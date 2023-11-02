// connects to redis server running locally
import redis from 'redis';
import util from 'util';

const client = redis.createClient();
const youPromised = util.promisify(client.get).bind(client);
client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  let newResponse = await youPromised(schoolName)
    console.log(newResponse);
  }

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
