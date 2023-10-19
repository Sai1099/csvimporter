from flask import Flask, render_template, request
import pandas as pd

import pandas as pd
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
            # Check if the file is an Excel file (e.g., .xlsx)
    file.filename.endswith('.xlsx')
                # Load the Excel file into a DataFrame
df = pd.read_excel(file, engine='openpyxl')

                # Do something with the DataFrame (e.g., print the first 5 rows)
             

client = MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
db = client['sai']  # Replace with your database name
collection = db['orginalphone']  # Replace with your collection name

   # Convert DataFrame to a lst of dictionaries (one dictionary per row)
data = df.to_dict(orient='records')

   # Insert the data into MongoDB
collection.insert_many(data)


   # Close the MongoDB connection
client.close()
render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
