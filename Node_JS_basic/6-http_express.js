// creates a small Express server

const express = require('express');
let port = 1245;

const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!')
})

app.listen(port);
