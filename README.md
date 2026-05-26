# Engineering Context AI

> Voice → Context → Memory → Retrieval → Understanding

Engineering Context AI is a voice-powered memory system built for engineering students who often remember **what they used**, but forget **why they used it**.

Traditional note-taking stores formulas.

This system stores **engineering reasoning**.

Example:

Voice input:

"Used Dijkstra because graph weights are positive."

Weeks later:

"When should Bellman Ford be used?"

The system retrieves previous reasoning context and provides engineering-aware answers.

---

## Problem

Engineering students constantly make decisions while solving problems:

- Why Dijkstra instead of Bellman Ford?
- Why Laplace Transform instead of Fourier?
- Why Kirchhoff Current Law here?
- Why this mechanical formula instead of another?

Those decisions disappear after assignments, labs, lectures, and exams.

Engineering Context AI creates a persistent engineering memory layer.

---

## Features

### Voice Engineering Memory

Capture engineering reasoning directly from voice.

Examples:

- "Used Bellman Ford because graph contains negative edges"
- "Laplace Transform converts signals to frequency domain"
- "Kirchhoff Current Law because current entering equals current leaving"

---

### Semantic Retrieval

Search engineering memory naturally.

Example:

Input:

```

negative graph weights

```

Output:

```

Bellman Ford → Handles negative weights

```

---

### Context-Aware Engineering Memory

Stores:

- Subject
- Concept
- Reasoning
- Timestamp
- Semantic embedding

Not formula storage.

Reasoning storage.

---

### Engineering Comparison Agent

Examples:

Compare:

```

Dijkstra vs Bellman Ford

```

Compare:

```

DFS vs BFS

```

Compare:

```

Laplace Transform vs Fourier Transform

```

---

### Timeline System

Visual chronological memory timeline:

```

DSA → Dijkstra → Positive weights

Signals → Laplace Transform

Electronics → Kirchhoff Current Law

```

---

### Analytics Dashboard

Track:

- Subject distribution
- Most used concepts
- Learning patterns
- Engineering memory growth

---

## Tech Stack

### Backend

- FastAPI
- Qdrant Cloud
- Sentence Transformers
- Lyzr
- Omi
- Streamlit

---

## Architecture

```

Omi Voice Input
|
v

Engineering Cleanup Layer
|
v

FastAPI Backend
|
+---------------------+
|                     |

v                     v

Lyzr Agent      Engineering Rules
|
v

Embedding Model
|
v

Qdrant Cloud
(Vector Memory)
|
v

Retrieval + Ranking
|
v

Streamlit Frontend

```

---

## Folder Structure

```

Engineering-Context-AI/

agents/
comparison_agent.py
context_agent.py
explanation_agent.py
lyzr_client.py

app/
routes/
analytics.py
reasoning.py
retrieval.py
timeline.py
voice.py

memory/
embeddings.py
qdrant_client.py

schemas/
reasoning_schema.py

services/
guardrails.py
memory_ranker.py
token_budget.py
context_optimizer.py
engineering_dictionary.py

frontend/
streamlit_app.py

requirements.txt
render.yaml

README.md

```

---

## Setup

Clone repository:

```bash
git clone https://github.com/AKing-283/Engineering-Context-AI

cd Engineering-Context-AI
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env

QDRANT_URL=

QDRANT_API_KEY=

HF_TOKEN=

LYZR_API_KEY=

```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger:

```

http://127.0.0.1:8000/docs

```

---

## Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## Omi Integration

Start backend:

```bash
uvicorn app.main:app --reload
```

Expose locally:

```bash
lt --port 8000
```

Example:

```

https://your-url.loca.lt

```

Set webhook in Omi:

```

https://your-url.loca.lt/omi-webhook

```

Voice example:

```

Used Bellman Ford because graph contains negative edges

```

System automatically:

- Cleans transcription
- Detects engineering subject
- Generates embeddings
- Stores semantic memory
- Enables future retrieval

---

## API Endpoints

### Store Memory

POST

```

/store-reasoning

```

Request:

```json
{
"subject":"DSA",
"text":"Used Dijkstra because graph weights are positive"
}
```

---

### Retrieve Memory

POST

```

/retrieve

```

Request:

```json
{
"query":"negative graph weights"
}
```

---

### Engineering Answer Agent

POST

```

/answer

```

Request:

```json
{
"query":"When should Bellman Ford be used?"
}
```

---

### Analytics

GET

```

/analytics

```

---

### Timeline

GET

```

/timeline

```

---

### Compare Concepts

POST

```

/compare

```

Request:

```json
{
"a":"Dijkstra",
"b":"Bellman-Ford"
}
```

---

## Why This Project Matters

Engineering students don't only need notes.

They need context.

This system preserves engineering reasoning so knowledge becomes reusable rather than disposable.

The goal is not replacing learning.

The goal is helping students remember *why they made technical decisions.*

---

## Future Improvements

- Multi-user authentication
- Personalized learning insights
- Engineering concept graph visualization
- Revision recommendations
- Engineering interview preparation mode
- PDF lecture memory ingestion

---

## Built For

Hackathon Theme:

**Autonomous AI Systems + Voice + Persistent Memory**

Core requirements used:

- Omi → Voice input
- Qdrant → Semantic memory
- Lyzr → AI reasoning and orchestration

---

## Author

Built with Engineering Students in mind.
