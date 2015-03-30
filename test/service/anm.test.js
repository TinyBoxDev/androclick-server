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

var mocha = require('mocha');
var chai = require('chai');
var should = chai.should();

var rewire = require('rewire');

var HTTP = require('../mocks.js').HTTP;
var ClientRequest = require('../mocks.js').ClientRequest;
var ClientResponse = require('../mocks.js').ClientResponse;
var ForecastMessage = require('../mocks.js').ForecastMessage;
var ForecastData = require('../data.js').Forecast;

describe('The ANM service', function() {

  var uut;
  var http;
  var forecastMessage;
  var request;
  var response;

  beforeEach(function(done) {
    var ANM = rewire('../../lib/service/anm.js');
    http = HTTP.clone();
    forecastMessage = new ForecastMessage();
    ANM.__set__('http', http);
    ANM.__set__('ForecastMessage', forecastMessage);
    uut = new ANM();

    request = new ClientRequest();
    response = new ClientResponse();

    done();
  });

  it('should get forecasts by stop', function(done) {
    response.on = function(event, callback) {
      if(event === 'data')
        callback(ForecastData);
      if(event === 'end')
        callback();
    };

    forecastMessage.parse = function(xml, callback) {
      xml.should.be.equal(ForecastData);
      callback(forecastMessage);
    };

    http.request = function(options, callback) {
      options.host.should.be.equal('m.anm.it');
      options.path.should.be.equal('/srv/ServiceInfoAnmLinee.asmx/CaricaPrevisioni?Palina=9999');
      options.method.should.be.equal('GET');
      request.setCallback(callback, response);
      return request;
    };

    var onData = function(data) {
      data.should.be.equal(forecastMessage);
      done();
    };

    uut.getForecasts(9999, onData);
  });

});
