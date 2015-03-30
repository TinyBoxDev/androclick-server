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

var ExpressApp = function MockExpressApp() {
  this.postCallbacks = {};
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

exports.HTTP = HTTP;
