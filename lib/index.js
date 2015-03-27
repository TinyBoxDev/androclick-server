var express = require('express');
var app = express();

var PORT = process.env.PORT || 5000;

var server = app.listen(PORT, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
