from flask import Flask, render_template
from pymongo import MongoClient

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

    # Agar picture field na mile to default image use kare
    if data and "picture" not in data:
        data["picture"] = "default.jpeg"

    return render_template("index.html", data=data)


# ==============================
# Run Server
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
