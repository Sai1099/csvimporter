from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection settings
mongo_uri = 'mongodb://localhost:27017'
database_name = 'sai'
collection_name = 'orginalphone'

@app.route('/')
def display_files():
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    files = list(collection.find(id='6530bd330789976774923a25'))

    return render_template('display.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)

