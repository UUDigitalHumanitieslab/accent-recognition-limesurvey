var express = require('express');
var path = require('path');
https = require('https');
var fs = require('fs');
var app = express();



// Define the port to run on
app.set('port', 3000);

app.use(express.static(path.join(__dirname, 'name-face')));

app.use(express.static(path.join(__dirname, 'dialect')));

https.createServer({
    key: fs.readFileSync('encryption/key.pem'),
    cert: fs.readFileSync('encryption/cert.pem')
}, app).listen(3000);

