/**
 *  _____ _            ______            ______ 
 * |_   _(_)           | ___ \           |  _  \
 *   | |  _ _ __  _   _| |_/ / _____  __ | | | |_____   __
 *   | | | | '_ \| | | | ___ \/ _ \ \/ / | | | / _ \ \ / /
 *   | | | | | | | |_| | |_/ / (_) >  <  | |/ /  __/\ V /
 *   \_/ |_|_| |_|\__, \____/ \___/_/\_\ |___/ \___| \_/
 *                __/ |
 *               |___/
 **/

/* jshint evil:true */

var mocha = require('mocha');
var chai = require('chai');
var should = chai.should();

var rewire = require('rewire');

var HTTP = require('../mocks.js').HTTP;
var ForecastData = require('../data.js').Forecast;

describe('The ANM service', function() {

  var uut;
  var http;

  beforeEach(function(done) {
    uut = rewire('../../lib/service/anm.js');
    http = eval('(' + HTTP.toString() + ')'); // this is used to clone the HTTP function
    uut.__set__('http', http);

    done();
  });

  it('should get forecasts by stop', function(done) {
    console.log(ForecastData);
    done();
  });

});
