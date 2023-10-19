// Backend (server.js)
const express = require('express');
const mongodb = require('mongodb');

const app = express();
const port = 3000;

const MongoClient = mongodb.MongoClient;
const url = 'mongodb://localhost:27017'; // Connection URL

app.get('/items', async (req, res) => {
  const client = new MongoClient(url, { useUnifiedTopology: true });
  
  try {
    await client.connect();
    const db = client.db('sai');
    const items = await db.collection('items').find({}).toArray();
    res.json(items);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching data');
  } finally {
    client.close();
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
