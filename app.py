from flask import Flask, render_template
from pymongo import MongoClient
import os

# Flask app initialize
app = Flask(__name__)

# ==============================
# MongoDB Atlas Connection
# ==============================
try:
    client = MongoClient(
        "mongodb+srv://aryannmishra65_db_user:T6AkVXVMvcptrbhl@cluster0.67bu29o.mongodb.net/?retryWrites=true&w=majority",
        serverSelectionTimeoutMS=5000,
        tlsAllowInvalidCertificates=True
    )
    db = client["portfolioDB"]
    collection = db["user"]
    # Test connection
    client.server_info()
    print("MongoDB connected successfully")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    collection = None

# ==============================
# Home Route
# ==============================
@app.route("/")
def index():
    # Default data
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
    
    # Try to fetch from MongoDB if connected
    if collection:
        try:
            mongo_data = collection.find_one()
            if mongo_data:
                data = mongo_data
        except Exception as e:
            print(f"Error fetching from MongoDB: {e}")
    
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
