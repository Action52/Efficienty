var express = require('express');
var path =  require('path');

var PORT = 5000;

var app=express()

app.use('/bootstrap', express.static(path.join(__dirname, './bootstrap')));

app.use('/img', express.static(path.join(__dirname, './img')));

app.use('/app', express.static(path.join(__dirname, './app')));

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});


app.listen(PORT);

console.log('Running on port ' + PORT);
