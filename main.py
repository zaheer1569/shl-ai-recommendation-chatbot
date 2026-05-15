from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form
from pydantic import BaseModel
from recommender import recommend

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<html>
<head>
    <title>SHL AI Chatbot</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .chat-container {
            width: 70%;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #222;
        }
        .bot-message {
            background: #eef3ff;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            line-height: 1.6;
        }
        .input-area {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        input {
            flex: 1;
            padding: 14px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        button {
            padding: 14px 24px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1>SHL AI Recommendation Chatbot</h1>
        <div class="bot-message">
            👋 Hello! I can help you find SHL assessments.
            <br><br>
            Try searches like:
            <br>
            • Python Developer
            <br>
            • Java Backend Engineer
            <br>
            • Data Analyst
            <br>
            • Cognitive Skills
        </div>
        <form action="/chat-ui" method="post">
            <div class="input-area">
                <input
                    type="text"
                    name="query"
                    placeholder="Type your role or skill..."
                    required
                >
                <button type="submit">Send</button>
            </div>
        </form>
    </div>
</body>
</html>
"""


@app.post("/chat-ui", response_class=HTMLResponse)
def chat_ui(query: str = Form(...)):
    results = recommend(query)

    if not results:
        return f"""
<html>
<body style="font-family:Arial;padding:40px;">
    <h2>No assessments found for "{query}"</h2>
    <a href="/">Go Back</a>
</body>
</html>
"""

    html = f"""
<html>
<head>
    <title>Results</title>
</head>
<body style="font-family:Arial;padding:40px;background:#f4f4f4;">
    <div style="
        background: #e9f3ff;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    ">
        <b>🤖 SHL AI Assistant</b><br><br>
        Here are the best assessment recommendations for:
        <b>{query}</b>
    </div>
"""

    for item in results:
        html += f"""
    <div style="
        background: white;
        padding: 20px;
        margin: 20px 0;
        border-radius: 12px;
        box-shadow: 0 0 8px rgba(0,0,0,0.08);
    ">
        <h2>{item.get("name", "SHL Assessment")}</h2>
        <a href="{item.get("url", "#")}" target="_blank">View Assessment</a>
        <p>{item.get("description", "")[:250]}...</p>
    </div>
"""

    html += """
    <br><br>
    <a href="/" style="
        padding: 12px 20px;
        background: #007bff;
        color: white;
        text-decoration: none;
        border-radius: 8px;
    ">
        ← Back to Chat
    </a>
</body>
</html>
"""
    return html


@app.post("/chat")
def chat(request: ChatRequest):
    latest_message = request.messages[-1].content

    results = recommend(latest_message)

    recommendations = []

    for item in results:
        recommendations.append({
            "name": item.get("name", "SHL Assessment"),
            "url": item.get("url", ""),
            "description": item.get("description", "")[:250]
        })

    return {
        "reply": "Here are some recommended SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }