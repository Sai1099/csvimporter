const express = require('express');
const multer = require('multer');
const XLSX = require('xlsx');
const MongoClient = require('mongodb').MongoClient;

const app = express();
const port = 3000;

const storage = multer.memoryStorage();

const upload = multer({ storage: storage,
    limits: { fileSize: 10 * 1024 * 1024 }});
    



// MongoDB connection URL and database name
const mongoURL = 'mongodb://localhost:27017';
const dbName = 'sai';

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/upload', upload.single('file'), (req, res) => {
    const buffer = req.file.buffer;

    // Parse the Excel file
    const workbook = XLSX.read(buffer, { type: 'buffer' });
    const sheetName = workbook.SheetNames[0];
    const data = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName]);

    // Save the data to MongoDB
    MongoClient.connect(mongoURL, (err, client) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error connecting to MongoDB');
            return;
        }

        const db = client.db(dbName);
        const collection = db.collection('orginalphone');

        collection.insertMany(data, (err, result) => {
            if (err) {
                console.error(err);
                res.status(500).send('Error saving data to MongoDB');
            } else {
                res.send('Data uploaded and saved to MongoDB successfully');
            }
            client.close();
        });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
