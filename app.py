from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://aryannmishra65_db_user:T6AkVXVMvcptrbhl@cluster0.67bu29o.mongodb.net/?appName=Cluster0")
db = client["aryandb"]

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
