from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Configure the MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client["sai"]
collection = db["orginalphone"]

@app.route('/')
def index():
    # Fetch data from the MongoDB collection
    data = collection.find_one({})  # You can add more specific query conditions here

    return render_template('text.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


