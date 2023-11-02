// arrays and functions, oh my!
const express = require('express');
import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);
const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
    let item = listProducts.find((item) => item.id === id);
    return item;
  }

const app = express();


app.listen(1245, () => {
    console.log(`Server is running on port 1245`);
  });
