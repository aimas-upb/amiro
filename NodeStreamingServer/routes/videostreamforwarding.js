var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
    // http://somewhere.com/noo.bin
    var remoteUrl = "http://admin:admin@192.168.0.127/video/mjpg.cgi";
    request(remoteUrl).pipe(res);
});

module.exports = router;