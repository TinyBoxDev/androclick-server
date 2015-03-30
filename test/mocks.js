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
 * Mock suite for node server side testing.
 **/

Function.prototype.clone = function() {
  var self = this;
  var temp = function temporary() { return self.apply(this, arguments); };
  for(var key in this) {
    if (this.hasOwnProperty(key))
      temp[key] = this[key];
  }
  return temp;
};

var ExpressApp = function MockExpressApp() {
  this.postCallbacks = {};
  this.getCallbacks = {};
};

ExpressApp.prototype.get = function(url, callback) {
  this.getCallbacks[url] = callback;
};

ExpressApp.prototype.post = function(url, callback) {
  this.postCallbacks[url] = callback;
};

exports.ExpressApp = ExpressApp;

var Request = function MockRequest() {
  this.params = {};
};

exports.Request = Request;

var Response = function MockResponse() {
};

Response.prototype.json = function() {
};

exports.Response = Response;

var ANM = function MockANM() {
};

ANM.prototype.getForecasts = function(number) {
};

exports.ANM = ANM;

var HTTP = function() {
};

HTTP.get = function() {
};

HTTP.request = function() {
};

exports.HTTP = HTTP;

var ClientRequest = function() {
  this.events = {};
  this.callback = null;
  this.response = null;
};

ClientRequest.prototype.on = function(event, callback) {
  this.events[event] = callback;
};

ClientRequest.prototype.setCallback = function(callback, response) {
  this.callback = callback;
  this.response = response;
};

ClientRequest.prototype.end = function() {
  this.callback(this.response);
};

exports.ClientRequest = ClientRequest;

var ClientResponse = function() {
  this.events = {};
};

ClientResponse.prototype.on = function(event, callback) {
  this.events[event] = callback;
};

exports.ClientResponse = ClientResponse;

var ForecastMessage = function() {
};

ForecastMessage.parse = function(xml) {
};

exports.ForecastMessage = ForecastMessage;
