import express from 'express';
import redis from 'redis';
import { promisify } from 'util';


const app = express();
const port = 1245;

// Initialize Redis client
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

async function storeListProductsInRedis() {
    try {
      await setAsync('listProducts', JSON.stringify(listProducts));
      console.log('List of products stored in Redis');
    } catch (error) {
      console.error('Error storing listProducts in Redis:', error);
    }
  }

  storeListProductsInRedis();