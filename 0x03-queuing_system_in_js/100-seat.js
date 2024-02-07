import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

const express = require('express');

const client = createClient();
const queue = createQueue();
client.get = promisify(client.get);

client.on('error', err => console.log('Redis client not connected to the server:', err.toString()));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveSeat(number) {
   await setAsync('available_seats', number.toString());
}
reserveSeat(50);

let reservationEnabled = true;

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const app = express();
const port  = 1245;

app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getAsync('available_seats');
   console.log('available seats', numberOfAvailableSeats);
   res.json({numberOfAvailableSeats});
});