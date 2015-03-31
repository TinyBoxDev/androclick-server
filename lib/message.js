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
 * Message.
 *
 * This module implements all Androclick messages.
 **/

'use strict';

var inherit = require('util').inherits;
var Parser = require('xml2js');

/**
 * ForecastMessage
 * This class implements the Androclick forecast message.
 **/
var ForecastMessage = function() {
};

/**
 * parse
 * This method converts an ANM message (based on xml) in
 * an Androclick message (based on JSON).
 *
 * @param {String} string is the xml message.
 * @param {Function} onDone is the callback fired when the convertion ends.
 **/
ForecastMessage.parse = function(string, onDone) {
  var onParsed = function(error, response) {
    if(response.ArrayOfPrevisione.Previsione[0].stato)
      return onDone(null, { code: 0, message: 'Invalid stop number' });

    var message = [];
    var array = response.ArrayOfPrevisione.Previsione;
    for(var index in array) {
      var forecast = {};
      forecast.line = array[index].linea[0];
      forecast.stopname = array[index].nome[0];
      forecast.stopnumber = array[index].id[0];
      forecast.time = array[index].time[0].replace('.', ':');
      forecast.arrivaltime = array[index].timeMin[0];
      message.push(forecast);
    }
    onDone(message);
  };

  Parser.parseString(string, onParsed);
};

exports.ForecastMessage = ForecastMessage;
