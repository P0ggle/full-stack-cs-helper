from flask import Flask
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "full-stack-cs-helper"

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client[DB_NAME]


if __name__ == "__main__":
    app.run(debug=True)
