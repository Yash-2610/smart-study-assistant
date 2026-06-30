# 📚 Smart Study Assistant

An AI-powered Study Assistant that helps students learn efficiently from their study materials using **RAG (Retrieval-Augmented Generation)**, **LangGraph**, **Groq LLM**, and **Streamlit**.

Upload one or more PDF notes and interact with them through natural language. The assistant can answer questions, generate summaries, quizzes, and flashcards based only on the uploaded study material.

---

## ✨ Features

-  Upload multiple PDF documents
-  AI-powered Question Answering (RAG)
-  Automatic Note Summarization
- Quiz Generation (MCQs)
-  Flashcard Generation
-  Source-aware responses
-  Search across all uploaded PDFs or a selected document
-  LangGraph-based agent orchestration
-  Interactive Streamlit interface

---

## 🏗️ Project Architecture

```
                +----------------------+
                |   Streamlit UI       |
                +----------+-----------+
                           |
                           v
                  +------------------+
                  |   LangGraph      |
                  |   Router Agent   |
                  +--------+---------+
                           |
         ------------------------------------------
         |                |             |          |
         v                v             v          v
      RAG Tool      Summary Tool   Quiz Tool  Flashcard Tool
         |                |             |          |
         +----------------+-------------+----------+
                          |
                          v
                Chroma Vector Database
                          |
                          v
               HuggingFace Embeddings
                          |
                          v
                  Uploaded PDF Documents
```

---

# 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangGraph
- LangChain

### LLM
- Groq API
- Llama 3.3 70B Versatile

### Embeddings
- sentence-transformers/all-MiniLM-L6-v2

### Vector Database
- ChromaDB

### Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter

---

# 📂 Folder Structure

```
Smart-Study-Assistant
│
├── backend
│   ├── agent.py
│   ├── config.py
│   ├── graph.py
│   ├── nodes.py
│   └── state.py
│
├── frontend
│   ├── app.py
│   └── upload_handler.py
│
├── rag
│   ├── ingest.py
│   ├── retriever.py
│   └── qa.py
│
├── tools
│   ├── summary_tool.py
│   ├── quiz_tool.py
│   └── flashcard_tool.py
│
├── uploads
├── vectorstore
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Yash-2610/smart-study-assistant.git
```



---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run frontend/app.py
```

---

# 🚀 Usage

1. Launch the application.
2. Upload one or more PDF documents.
3. Click **Process Documents**.
4. Select either:
   - All Documents
   - A specific uploaded document
5. Ask questions naturally.
6. Generate:
   - Summary
   - Quiz
   - Flashcards

---

# 💬 Example Queries

### Question Answering

```
What is DBMS?
```

```
Explain Deadlock in Operating Systems.
```

```
Difference between Process and Thread.
```

---

### Summary

```
Summarize this document.
```

```
Summarize DBMS.
```

---

### Quiz

```
Generate a quiz on Operating Systems.
```

---

### Flashcards

```
Generate flashcards for Database Management System.
```

---

# 🧠 Agent Workflow

The application uses **LangGraph** for agent orchestration.

### Router Agent

Analyzes the user's request and selects the appropriate tool.

Possible tools:

- RAG
- Summary
- Quiz
- Flashcards

The selected tool retrieves the required information and returns the final response to the user.

---

# 🔄 RAG Pipeline

```
PDF Upload
      │
      ▼
PyPDFLoader
      │
      ▼
Text Chunking
      │
      ▼
Embeddings
      │
      ▼
Chroma Vector Store
      │
      ▼
Retriever
      │
      ▼
Groq LLM
      │
      ▼
Answer
```

---

# 🌟 Key Features Implemented

- Retrieval-Augmented Generation (RAG)
- LangGraph Agent Orchestration
- Multi-document support
- Multiple AI tools
- Source-aware answers
- State management
- Modular architecture
- Streamlit UI

---

# 📌 Future Improvements

- Conversation memory
- Chat history persistence
- User authentication
- PDF highlighting
- Image support
- OCR for scanned PDFs
- Export summaries as PDF
- Spaced repetition for flashcards
- Deployment with persistent cloud storage

---
