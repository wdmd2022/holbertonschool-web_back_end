// creates a redis client
import redis from 'redis';
import util from 'util';

const client = redis.createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
    console.log(`Received message on channel ${channel}: ${message}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
})
