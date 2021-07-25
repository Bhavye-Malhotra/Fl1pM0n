const express = require("express");
const database = require("./database.js"); 
const app = express(); 
const path = require("path");

app.use(express.static(__dirname + '/public'));

app.get('/data', function(req, res) {
    database.run(req.query.search).then(function(data) {
        console.log(data);
        res.send(data);
    });
});

app.listen(8080); 
console.log("Server running at Port 8080");
