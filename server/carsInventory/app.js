/*jshint esversion: 8 */

const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3050;

app.use(cors());
app.use(express.urlencoded({ extended: false }));

const carsData = JSON.parse(fs.readFileSync('car_records.json', 'utf8'));

mongoose.connect('mongodb://mongo_db:27017/', { dbName: 'dealershipsDB' })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));


const Cars = require('./inventory');

try {

  Cars.deleteMany({}).then(() => {
    Cars.insertMany(carsData.cars);
  });
} catch (error) {
  console.error(error);
  // Handle errors properly here
}

app.get('/', async (req, res) => {
  res.send('Welcome to the Mongoose API');
});



app.get('/cars/:id', async (req, res) => {
    try {
      const dealerId = parseInt(req.params.id);  // 👈 Convert to number
      const documents = await Cars.find({ dealer_id: dealerId });
      res.json(documents);
    } catch (error) {
      console.error("Error fetching reviews:", error);
      res.status(500).json({ error: 'Error fetching reviews' });
    }
  });
  
  app.get('/carsbymake/:id/:make', async (req, res) => {
    try {
      const dealerId = parseInt(req.params.id);
      const documents = await Cars.find({
        dealer_id: dealerId,
        make: req.params.make
      });
      res.json(documents);
    } catch (error) {
      res.status(500).json({ error: 'Error fetching reviews by car make' });
    }
  });
  
  app.get('/carsbymodel/:id/:model', async (req, res) => {
    try {
      const dealerId = parseInt(req.params.id);
      const documents = await Cars.find({
        dealer_id: dealerId,
        model: req.params.model
      });
      res.json(documents);
    } catch (error) {
      res.status(500).json({ error: 'Error fetching reviews by model' });
    }
  });
  
  app.get('/carsbymaxmileage/:id/:mileage', async (req, res) => {
    try {
      const dealerId = parseInt(req.params.id);
      const mileage = parseInt(req.params.mileage);
  
      let condition = {};
      if (mileage === 50000) condition = { $lte: mileage };
      else if (mileage === 100000) condition = { $lte: mileage, $gt: 50000 };
      else if (mileage === 150000) condition = { $lte: mileage, $gt: 100000 };
      else if (mileage === 200000) condition = { $lte: mileage, $gt: 150000 };
      else condition = { $gt: 200000 };
  
      const documents = await Cars.find({
        dealer_id: dealerId,
        mileage: condition
      });
      res.json(documents);
    } catch (error) {
      res.status(500).json({ error: 'Error fetching by mileage' });
    }
  });
  
  app.get('/carsbyprice/:id/:price', async (req, res) => {
    try {
      const dealerId = parseInt(req.params.id);
      const price = parseInt(req.params.price);
  
      let condition = {};
      if (price === 20000) condition = { $lte: price };
      else if (price === 40000) condition = { $lte: price, $gt: 20000 };
      else if (price === 60000) condition = { $lte: price, $gt: 40000 };
      else if (price === 80000) condition = { $lte: price, $gt: 60000 };
      else condition = { $gt: 80000 };
  
      const documents = await Cars.find({
        dealer_id: dealerId,
        price: condition
      });
      res.json(documents);
    } catch (error) {
      res.status(500).json({ error: 'Error fetching by price' });
    }
  });
  
  app.get('/carsbyyear/:id/:year', async (req, res) => {
    try {
      const dealerId = parseInt(req.params.id);
      const year = parseInt(req.params.year);              // convert here too
  
      const documents = await Cars.find({
        dealer_id: dealerId,
        year: { $gte: year }
      });
      res.json(documents);
    } catch (error) {
      res.status(500).json({ error: 'Error fetching by year' });
    }
  });
  
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});    