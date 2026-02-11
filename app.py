from flask import Flask, render_template
from pymongo import MongoClient
import os

# Flask app initialize
app = Flask(__name__)

# ==============================
# MongoDB Atlas Connection
# ==============================
client = MongoClient(
    "mongodb+srv://aryannmishra65_db_user:T6AkVXVMvcptrbhl@cluster0.67bu29o.mongodb.net/?retryWrites=true&w=majority"
)

# Database and Collection
db = client["portfolioDB"]
collection = db["user"]

# ==============================
# Home Route
# ==============================
@app.route("/")
def index():
    # Fetch single document from MongoDB
    data = collection.find_one()

    # Agar data na mile to default data use kare
    if not data:
        data = {
            "name": "Aryan Mishra",
            "role": "Full Stack Developer",
            "about": "Passionate developer creating amazing web applications.",
            "picture": "WhatsApp Image 2026-02-10 at 5.46.19 PM.jpeg",
            "skills": ["Python", "Flask", "MongoDB", "JavaScript", "HTML/CSS"],
            "projects": [
                {"title": "Portfolio Website", "description": "Flask-based portfolio with MongoDB"},
                {"title": "Expense Tracker", "description": "Track expenses with MongoDB backend"}
            ],
            "email": "aryan@example.com"
        }
    
    # Agar picture field na mile to default image use kare
    if "picture" not in data:
        data["picture"] = "WhatsApp Image 2026-02-10 at 5.46.19 PM.jpeg"

    return render_template("index.html", data=data)


# ==============================
# Run Server
# ==============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
