from bson import ObjectId
from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.cs_helper
crates = db.crates
skin_collections = db.skin_collections
skins = db.skins
