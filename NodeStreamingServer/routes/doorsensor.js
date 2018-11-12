var express = require('express');
var router = express.Router();

router.post('/events', function(req, res) {
    console.log(req.body);
});

router.post('/', function(req, res) {
    console.log(req.body);
});

module.exports = router;
