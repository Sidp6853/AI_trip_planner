# 🧭 AI Trip Planner

An intelligent **AI-powered travel itinerary generator** built using **Streamlit**, **FastAPI**, and **Groq API (LLM)**.  
Just enter your travel query in natural language like *"plan a 5 days trip to Goa"*, and the app instantly creates a **personalized trip plan** — with day-wise recommendations, attractions, and activities using an advanced agentic workflow.

---

## 🚀 Features

- 🌍 **Natural Language Processing** — Simply describe your travel plans in plain English.  
- 🤖 **Agentic Workflow** — Powered by LangGraph for intelligent multi-agent orchestration.  
- ⚡ **Lightning-Fast Generation** — Groq API delivers instant AI-powered itineraries.  
- 🎯 **Personalized Planning** — Tailored recommendations based on your preferences.  
- 🖥️ **Modern Architecture** — FastAPI backend with Streamlit frontend for seamless experience.  
- 📊 **Workflow Visualization** — Automatic generation of agent workflow graphs.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Framework | LangGraph |
| LLM Provider | Groq API |
| Language | Python 3.8+ |
| Environment | python-dotenv |

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sidp6853/AI_trip_planner.git
   cd AI_trip_planner
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🏃 Running the Application

### Start the Backend (FastAPI)

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

**API Endpoint:**
- `POST /query` - Submit travel planning queries

**Example Request:**
```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "plan a 5 days trip to Goa"}'
```

### Start the Frontend (Streamlit)

In a separate terminal:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser at `http://localhost:8501`

---

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for LLM access | Yes |

---

## 💡 Usage

1. Open the Streamlit interface in your browser
2. Enter your travel query in natural language:
   - *"Plan a 7-day cultural trip to Kyoto, Japan"*
   - *"Create a budget-friendly 3-day itinerary for Paris"*
   - *"Plan a 5 days adventure trip to Goa"*
3. Click the **'Send'** button
4. Watch the AI agents generate your personalized itinerary
5. View the detailed day-by-day travel plan with recommendations

---

## 🏗️ Architecture

The application uses LangGraph to orchestrate intelligent agents:

```
User Query → FastAPI → LangGraph Workflow → Groq LLM → Personalized Itinerary
                ↓
          Workflow Graph
          (saved as PNG)
```

The agent workflow is automatically visualized and saved as `my_graph.png` with each request.

---

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for blazing-fast LLM inference
- [LangGraph](https://github.com/langchain-ai/langgraph) for powerful agentic workflows
- The open-source community for amazing tools and libraries

---

## 👩‍💻 Author

**Siddhi Pandya**

- GitHub: [@Sidp6853](https://github.com/Sidp6853)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ and AI

</div>