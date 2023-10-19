import pandas as pd
from pymongo import MongoClient
from gridfs import GridFS

   # Load Excel data into a DataFrame
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Read the uploaded file into a DataFrame
            df = pd.read_csv(uploaded_file)
            # You can also read Excel files with pd.read_excel(uploaded_file)

            # Do something with the DataFrame (e.g., print the first 5 rows)
            print(df.head())
            client = MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
            db = client['sai']  # Replace with your database name
            collection = db['orginalphone']  # Replace with your collection name

   # Convert DataFrame to a list of dictionaries (one dictionary per row)
            data = df.to_dict(orient='records')

   # Insert the data into MongoDB
            collection.insert_many(data)
            
            
   # Close the MongoDB connection
            
            files = list(collection.find())
            return render_template('display.html', files=files)
            
        client.close()

    return render_template('index.html')


# df = pd.read_excel('your_data.xlsx')  # or pd.read_csv('your_data.csv')

   # Connect to MongoDB



if __name__ == '__main__':
    app.run(debug=True)