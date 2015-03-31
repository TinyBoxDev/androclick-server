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
 * Stops resource.
 *
 * This module provides stop informations.
 * This resource is queried by using the "/stops/" URL prefix.
 **/

'use strict';

var ANM = require('../service/anm.js');

module.exports = function StopsResource(app) {

  app.get('/stops/:number', function(request, response) {
    console.log('Received a new forecast request for stop ' + request.params.number);

    var onData = function(data) {
      response.json(data);
    };

    var onError = function(error) {
      response.status(400).json(error);
    };

    var anm = new ANM();
    console.log('Contacting the ANM service');
    anm.getForecasts(request.params.number, onData, onError);
  });

};
