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
 * ANM service.
 *
 * This module implements the anm APIs.
 **/

'use strict';

var http = require('http');
var ForecastMessage = require('../message.js').ForecastMessage;

/**
 * ANM Service class
 *
 * This is the main class of this module.
 **/
var ANM = function ANM() {
  this.options = {
    host: 'm.anm.it',
    path: '/srv/ServiceInfoAnmLinee.asmx/'
  };
};

/**
 * getForecasts
 *
 * This method gets the buses forecast from the ANM server.
 * @param {Integer} stopNumber is the number of the stop where the forecast is performed on.
 * @param {Function} onData is the callback fired when the data is loaded
 **/
ANM.prototype.getForecasts = function(stopNumber, onData) {
  this.options.path += 'CaricaPrevisioni?Palina=' + stopNumber;
  this.options.method = 'GET';

  var onResponse = function(response) {
    console.log('Connected to the ANM server');

    var message = '';

    response.on('data', function(chunk) {
      console.log('New chunk received');
      message += chunk;
    });

    response.on('end', function() {
      console.log('Data received... Creating response');

      var onParsed = function(data) {
        console.log('Message ready. Calling the response callback');
        onData(data);
      };

      var forecastMessage = ForecastMessage.parse(message, onParsed);
    });
  };

  http.request(this.options, onResponse).end();
  console.log('Forecast request sent to url http://' + this.options.host + this.options.path);
};

module.exports = ANM;
