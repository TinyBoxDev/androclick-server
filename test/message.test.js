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

describe('The message module', function() {

  describe('The forecast message', function() {

    var ForecastMessage = rewire('../lib/message.js').ForecastMessage;
    var data = require('./data.js').Forecast;

    it('should parse the xml message', function(done) {
      var onParsed = function(object) {
        object.length.should.be.equal(3);
        object[0].line.should.be.equal('C41');
        object[0].stopname.should.be.equal('SEMMOLA-OSPEDALE PASCALE-LAB. ANALISI CARDILLO FRA');
        object[0].stopnumber.should.be.equal('3129');
        object[0].time.should.be.equal('14:49');
        object[0].arrivaltime.should.be.equal('5');
        done();
      };

      ForecastMessage.parse(data, onParsed);
    });

  });

});
