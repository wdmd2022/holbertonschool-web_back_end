// creates a small server using the http module

const http = require('http');

const hostname = '127.0.0.1';
const port = 1245;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

const app = server.listen(port, hostname);

module.exports = app;
