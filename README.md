# Multi AI Agent

A powerful multi-agent AI application built with Groq, LangGraph, Tavily Search, FastAPI, and Streamlit. This project provides an AI agent framework with web search capabilities, customizable system prompts, and support for multiple LLM models.

## 🌟 Features

- **Multiple LLM Support**: Works with Groq models (Llama-3.3-70B-versatile, GPT-OSS-120B)
- **Web Search Integration**: Tavily-powered search for real-time information
- **Agent Memory**: LangGraph-based conversation memory with checkpointer
- **Modern UI**: Streamlit-based frontend for easy interaction
- **RESTful API**: FastAPI backend for scalable backend services
- **Containerized**: Docker support for easy deployment
- **CI/CD Ready**: Jenkins pipeline for automated builds and deployments
- **Cloud Deployment**: AWS ECS Fargate deployment support

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Streamlit     │────▶│    FastAPI      │────▶│   LangGraph     │
│   (Frontend)    │     │   (Backend)     │     │   (AI Agent)    │
│   Port: 8501    │     │   Port: 8080    │     │                 │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                              ┌──────────────────────────┼──────────────────────────┐
                              │                          │                          │
                              ▼                          ▼                          ▼
                    ┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
                    │   ChatGroq      │        │  Tavily Search  │        │    Memory       │
                    │   (LLM)         │        │   (Web Search)  │        │   (Checkpoint)  │
                    └─────────────────┘        └─────────────────┘        └─────────────────┘
```

## 📁 Project Structure

```
multi-ai-agent/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── backend/
│   │   ├── __init__.py
│   │   └── fast_api.py         # FastAPI backend server
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py         # Application settings
│   ├── core/
│   │   ├── __init__.py
│   │   └── ai_agent.py         # LangGraph AI agent
│   ├── frontend/
│   │   ├── __init__.py
│   │   └── ui.py               # Streamlit UI
│   └── common/
│       ├── __init__.py
│       ├── logger.py           # Logging utility
│       └── custom_exception.py  # Custom exceptions
├── custom_jenkins/
│   └── Dockerfile              # Jenkins Docker image
├── Dockerfile                  # Application Docker image
├── Jenkinsfile                 # Jenkins CI/CD pipeline
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- API keys for Groq and Tavily

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Deebyendu/Multi-AI-Agent-With-Prompt.git
   cd Multi-AI-Agent-With-Prompt-
   ```

2. **Create and activate virtual environment**

   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   uv sync
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

5. **Run the application**

   ```bash
   python app/main.py
   ```

   The application will start:
   - **Frontend**: http://localhost:8501
   - **Backend API**: http://localhost:8080

### Running with Docker

1. **Build the Docker image**

   ```bash
   docker build -t multi-ai-agent .
   ```

2. **Run the container**

   ```bash
   docker run -d \
     --name multi-ai-agent \
     -p 8501:8501 \
     -p 8080:8080 \
     -e GROQ_API_KEY=your_groq_api_key \
     -e TAVILY_API_KEY=your_tavily_api_key \
     multi-ai-agent
   ```

   > Note: The Dockerfile uses `uv sync` for dependency installation.

## 🔧 Configuration

### Environment Variables

| Variable         | Description               | Required |
| ---------------- | ------------------------- | -------- |
| `GROQ_API_KEY`   | API key for Groq LLM      | Yes      |
| `TAVILY_API_KEY` | API key for Tavily search | Yes      |

### Supported Models

- `llama-3.3-70b-versatile`
- `openai/gpt-oss-120b`

## 📦 Dependencies

- **langchain-groq**: Groq LLM integration
- **langchain-community**: CommunityLangChain tools
- **langchain-core**: Core LangChain abstractions
- **langgraph**: Agent orchestration with graph-based workflow
- **langchain-tavily**: Tavily search integration
- **fastapi**: RESTful API framework
- **uvicorn**: ASGI server
- **streamlit**: Web UI framework
- **pydantic**: Data validation
- **python-dotenv**: Environment variable management

## 🧪 API Reference

### POST `/chat`

Send a chat message to the AI agent.

**Request Body:**

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "You are a helpful assistant.",
  "messages": ["Hello, how can you help me?"],
  "allow_search": true
}
```

**Response:**

```json
{
  "response": "Hello! I'd be happy to help you with..."
}
```

## 🛠️ Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
```

## 🚢 Deployment

### AWS ECS Fargate Deployment

The project includes a complete CI/CD pipeline for AWS ECS Fargate deployment:

1. **Jenkins CI/CD Pipeline Stages:**
   - Checkout code from GitHub
   - SonarQube code quality analysis
   - Build Docker image
   - Push image to AWS ECR
   - Deploy to AWS ECS Fargate

2. **Environment Variables for ECS:**

   ```
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

For detailed deployment instructions, see [FULL_DOCUMENTATION.md](FULL_DOCUMENTATION.md).

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Deebyendu Mondal**

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
