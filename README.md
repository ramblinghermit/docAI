# DocAI — AI Copilot for Collaborative Documents & Spreadsheets

> An intelligent document and spreadsheet workspace combining **UniverJS** with **Gemini LLM** to translate natural language prompts into structured document and sheet mutations in real-time.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue 3](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![UniverJS](https://img.shields.io/badge/UniverJS-Sheets%20%26%20Docs-blue)](https://univer.ai/)
[![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-8E75B2?logo=google)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

---

## 🚀 Overview

**DocAI** bridges conversational AI with interactive document and spreadsheet canvases. Instead of manually editing formulas, formatting cells, or structuring reports, users express their intent in natural language. DocAI's backend interprets the context and generates deterministic **Univer mutations** (`commandId`, `params`, `app_context`) that execute directly on the client canvas.

### Key Capabilities
- 📊 **Natural Language to Sheet Mutations**: Automatically format ranges, insert rows, compute aggregations, and manipulate cells via structured JSON schemas.
- ⚡ **Gemini-Powered Command Translation**: Translates user intent into validated `UniverCommand` payloads with strict Pydantic schemas.
- 🎨 **UniverJS Interactive Workspace**: High-performance canvas for rich text documents and spreadsheets.
- 🐳 **Docker-Ready Fullstack Architecture**: Containerized FastAPI backend, Vue 3 + Vite frontend, and PostgreSQL service.

---

## 🏗️ Project Architecture

```text
docAI/
├── backend/                   # FastAPI REST API & Gemini AI Service
│   ├── app/
│   │   ├── api/v1/routes.py   # AI command translator & health endpoints
│   │   ├── core/config.py     # Environment & settings configuration
│   │   ├── crud/              # Database operations
│   │   ├── db/                # Session & database initialization
│   │   ├── models/            # SQLAlchemy database models
│   │   └── schemas/           # Pydantic validation schemas
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                  # Vue 3 + Vite + UniverJS Workspace
│   ├── src/
│   │   ├── App.vue            # Core application layout
│   │   ├── views/             # Sheet and document views
│   │   └── router/            # Navigation routing
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml         # Multi-container orchestration
└── README.md
```

---

## ⚡ Quickstart

### 1. Configure Environment
```bash
cp backend/.env.example backend/.env
```
Add your Google Gemini API key to `backend/.env`:
```env
GEMINI_API_KEY="your-gemini-api-key"
```

### 2. Run with Docker Compose
```bash
docker-compose up --build
```
- **Frontend Workspace**: `http://localhost:3000`
- **FastAPI API & Docs**: `http://localhost:8000/docs`

---

### Manual Local Development

#### Backend (FastAPI)
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Unix:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

#### Frontend (Vue 3 + Vite)
```bash
cd frontend
npm install
npm run dev
```

---

## 📄 License
MIT License
