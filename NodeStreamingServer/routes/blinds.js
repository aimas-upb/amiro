var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('blinds', { title: 'Blinds' });
});

router.post('/', function(req, res) {

    console.log(req.body);
    if(req.body && req.body.id && req.body.command)
    {
        if(Number(req.body.id) === 1 || Number(req.body.id) === 2)
        {
            if(Number(req.body.command) === 1 || Number(req.body.command) === 0 || Number(req.body.command) === -1)
            {
                // Require rosnodejs itself
                var rosnodejs = require('rosnodejs');
                // Requires the std_msgs message package
                var std_msgs = rosnodejs.require('std_msgs').msg;

                const nh = rosnodejs.nh;
                const pub = nh.advertise('/blinds_' + req.body.id, 'std_msgs/Int32');
                pub.publish({ data: req.body.command });

                res.send("ok");
            }
            else{
                res.send("Invalid Command");
            }
        }
        else{
            res.send("Invalid ID");
        }
    }
    else{
        res.send("Invalid Request");
    }
});

module.exports = router;