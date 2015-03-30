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

var ExpressApp = require('../mocks.js').ExpressApp;
var Request = require('../mocks.js').Request;
var Response = require('../mocks.js').Response;
var ANM = require('../mocks.js').ANM;

describe('The stops resource', function() {

  var uut;
  var app;
  var req;
  var res;
  var anm;

  beforeEach(function(done) {
    uut = rewire('../../lib/resource/stop.js');
    anm = ANM.clone();
    uut.__set__('ANM', anm);

    app = new ExpressApp();
    uut(app);
    req = new Request();
    res = new Response();

    done();
  });

  it('should get the arriving buses by number', function(done) {
    var stubData = {};

    anm.prototype.getForecasts = function(number, onData) {
      number.should.be.equal(9999);
      onData(stubData);
    };

    req.params.number = 9999;

    res.json = function(data) {
      data.should.be.equal(stubData);
      done();
    };

    should.exist(app.getCallbacks['/stops/:number']);
    app.getCallbacks['/stops/:number'](req, res);
  });

});
