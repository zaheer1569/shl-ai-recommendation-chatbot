from flask import Flask, request
from recommender import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        query = request.form.get("query")
        results = recommend(query)

    html = """
<!DOCTYPE html>
<html>
<head>
    <title>SHL AI Recommendation System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 40px;
        }
        h1 {
            color: #222;
        }
        h2 {
            color: #111;
            margin-bottom: 10px;
        }
        form {
            margin-bottom: 30px;
        }
        input {
            width: 300px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            background: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .card {
            background: white;
            padding: 25px;
            margin-top: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>SHL AI Recommendation System</h1>
    <form method="POST">
        <input type="text" name="query" placeholder="Enter skill or role" required>
        <button type="submit">Search</button>
    </form>
"""

    if not results:
        html += "<p>No assessments found.</p>"

    for item in results:
        html += f"""
    <div class="card">
        <h2>{item.get('name') or 'SHL Assessment'}</h2>
        <a href="{item['url']}" target="_blank">View Assessment</a>
        <p>{item['description'][:250]}...</p>
    </div>
"""

    html += "</body></html>"
    return html


if __name__ == "__main__":
    app.run(debug=True)