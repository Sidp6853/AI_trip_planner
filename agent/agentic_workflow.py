from utils.model_loaders import ModelLoader
from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.calculator_tool import CalculatorTool
from tools.currency_convertor_tool import CurrencyConvertorTool
from tools.calculator_tool import CalculatorTool
from tools.arithmetic_tool import ArithmeticTool
from prompt_library import SYSYTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_conditions


class GraphBuilder():

    def __init__(self):
            def __init__(self,model_provider: str = "groq"):
                self.model_loader = ModelLoader(model_provider=model_provider)
                self.llm = self.model_loader.load_llm()
                
                self.tools = []
                
                self.weather_tools = WeatherInfoTool()
                self.place_search_tools = PlaceSearchTool()
                self.calculator_tools = CalculatorTool()
                self.currency_converter_tools = CurrencyConverterTool()
                
                self.tools.extend([* self.weather_tools.weather_tool_list, 
                                * self.place_search_tools.place_search_tool_list,
                                * self.calculator_tools.calculator_tool_list,
                                * self.currency_converter_tools.currency_converter_tool_list])
                
                self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
                
                self.graph = None
        
            
       

    def agent_fucntion(self, state: MessagesState):
        user_question = state["messages"]
        input_question = SYSYTEM_PROMPT + user_question
        response = self.llm_with_tools.invoke(input_question)
        return response
    
    def build_grapg(self):
        StateGraph(MessagesState)
        graph_builder.add_egde(START,"agent")
        graph_builder.add_node("agent", self.agent_fucntion)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_conditional_edges("agent",tools_conditions)
        graph_builer.add_edge("tools",END)

        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        pass
