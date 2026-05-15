# SHL AI Recommendation Chatbot — Final Submission Guide

## Project Overview

The SHL AI Recommendation Chatbot is a FastAPI-based web application that recommends SHL assessments based on user-entered roles or skills.

The system uses semantic similarity and embeddings to match user queries with relevant SHL assessments.

---

# Features

* FastAPI backend
* Interactive chatbot-style UI
* Semantic search recommendation system
* Dynamic HTML rendering
* SHL assessment recommendations
* REST API support
* Local deployment support

---

# Tech Stack

* Python
* FastAPI
* Sentence Transformers
* HTML/CSS
* Uvicorn

---

# Project Structure

```text
SHL-AI-Agent/
│
├── main.py
├── recommender.py
├── embeddings.py
├── scraper.py
├── catalog.json
├── embeddings.pkl
├── requirements.txt
└── README.md
```

---

# Installation Steps

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd SHL-AI-Agent
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Application

```bash
python -m uvicorn main:app --reload
```

---

# Application URLs

## Main UI

```text
http://127.0.0.1:8000
```

## Health Endpoint

```text
http://127.0.0.1:8000/health
```

## Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# Example Queries

* Python Developer
* Java Backend Engineer
* Data Analyst
* SQL
* Cognitive Skills

---

# API Example

## Endpoint

```text
POST /chat
```

## Request Body

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Python Developer"
    }
  ]
}
```

## Response

```json
{
  "reply": "Here are some recommended SHL assessments.",
  "recommendations": [
    {
      "name": "Assessment Name",
      "url": "Assessment URL",
      "description": "Assessment Description"
    }
  ],
  "end_of_conversation": false
}
```

---

# GitHub Upload Steps

## Initialize Git

```bash
git init
```

## Add Files

```bash
git add .
```

## Commit

```bash
git commit -m "SHL AI Recommendation Chatbot"
```

## Connect GitHub Repository

```bash
git remote add origin <your-github-repo-url>
```

## Push Code

```bash
git push -u origin main
```

---

# Deployment on Render

## Build Command

```text
pip install -r requirements.txt
```

## Start Command

```text
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# Final Submission Checklist

* Working FastAPI application
* Chatbot-style UI
* GitHub repository
* README.md file
* Deployment link
* Screenshots of working application
* API endpoint working
* Health endpoint working
* Swagger docs working

---

# Suggested Screenshots

1. Home chatbot UI
2. Python Developer results
3. Data Analyst results
4. Swagger API docs
5. Health endpoint

---

# Conclusion

This project demonstrates:

* Backend API development
* Semantic search implementation
* Recommendation systems
* FastAPI application development
* Frontend integration
* Deployment readiness
