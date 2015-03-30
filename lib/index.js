/**
 *  _____ _            ______            ______ 
 * |_   _(_)           | ___ \           |  _  \
 *   | |  _ _ __  _   _| |_/ / _____  __ | | | |_____   __
 *   | | | | '_ \| | | | ___ \/ _ \ \/ / | | | / _ \ \ / /
 *   | | | | | | | |_| | |_/ / (_) >  <  | |/ /  __/\ V /
 *   \_/ |_|_| |_|\__, \____/ \___/_/\_\ |___/ \___| \_/
 *                __/ |
 *               |___/
 *
 * Androclick Server entry-point.
 *
 * This module loads all the resource modules
 * and puts the http server listening.
 **/

'use strict';

var express = require('express');
var app = express();

var requiredir = require('require-directory');

// Loading controllers
var resources = requiredir(module, './resource');
for(var key in resources)
  resources[key](app);

// Starting the HTTP server
var PORT = process.env.PORT || 5000;
var server = app.listen(PORT, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Androclick app listening at http://%s:%s', host, port);
});
