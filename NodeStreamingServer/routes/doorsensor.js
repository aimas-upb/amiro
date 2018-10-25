var express = require('express');
var router = express.Router();

/* GET home page. */
app.post('/', function(req, res) {
    res.send(req.body);
});

module.exports = router;
