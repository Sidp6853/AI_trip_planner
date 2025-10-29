import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper


class GooglePlaceSearchTool:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.use_google = bool(self.api_key)

        # Get Tavily API key from environment
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")

        if self.use_google:
            self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=self.api_key)
            self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
            print("✅ Using Google Places API for place search.")   
        else:
            print("⚠️ Google Places API key missing — switching to Tavily.")
            # Initialize Tavily with API key
            if self.tavily_api_key:
                self.tavily_tool = TavilySearch(
                    api_key=self.tavily_api_key,
                    topic="general",
                    include_answer="advanced"
                )
            else:
                raise ValueError("TAVILY_API_KEY environment variable is not set!")

    def _tavily_fallback(self, query: str):
        result = self.tavily_tool.invoke({"query": query})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def google_search_attractions(self, place: str) -> dict:
        query = f"top attractive places in and around {place}"
        if self.use_google:
            return self.places_tool.run(query)
        else:
            return self._tavily_fallback(query)

    def google_search_restaurants(self, place: str) -> dict:
        query = f"what are the top 10 restaurants and what is the famous street food in and around {place}?"
        if self.use_google:
            return self.places_tool.run(query)
        else:
            return self._tavily_fallback(query)

    def google_search_activity(self, place: str) -> dict:
        query = f"Activities in and around {place}"
        if self.use_google:
            return self.places_tool.run(query)
        else:
            return self._tavily_fallback(query)

    def google_search_transportation(self, place: str) -> dict:
        query = f"What are the different modes of transportation available in {place}"
        if self.use_google:
            return self.places_tool.run(query)
        else:
            return self._tavily_fallback(query)


class TavilyPlaceSearchTool:
    def __init__(self):
        # Get API key once during initialization
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        if not self.tavily_api_key:
            raise ValueError("TAVILY_API_KEY environment variable is not set!")
        
        # Create a single instance to reuse
        self.tavily_tool = TavilySearch(
            api_key=self.tavily_api_key,
            topic="general",
            include_answer="advanced"
        )

    def tavily_search_attractions(self, place: str) -> dict:
        result = self.tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_restaurants(self, place: str) -> dict:
        result = self.tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_activity(self, place: str) -> dict:
        result = self.tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        result = self.tavily_tool.invoke({"query": f"What are the different modes of transportation available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result