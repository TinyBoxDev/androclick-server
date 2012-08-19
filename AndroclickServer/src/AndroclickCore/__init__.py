#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''

from cgi import parse_qs, escape;
from wsgiref import util;
import os, sys;
import WebResources;
from AndroclickCore.AndroclickController import AndroclickController;
from urllib import unquote;
from AndroclickCore.AndroclickObjectFactory.AndroclickObject import ValidationException as ValidationException;
import AndroclickCore.AndroclickObjectFactory as AndroclickObjectFactory;
from AndroclickCore.AndroclickObjectFactory.Response import Response;

class AndroclickCore(object): 
    # Androclick configuration file
    _properties = None;
    
    def __call__(self, environ, start_response):
        status = '200 OK';
        
        if environ['REQUEST_METHOD']=='GET':
            response, response_headers = self._get_page(environ);
        
        else:
            length = int(environ['CONTENT_LENGTH']);
            data = environ['wsgi.input'].read(length);
            response, response_headers = self._dispachRequest(data);
        
        start_response(status, response_headers);
        return [response];
    
    def _dispachRequest(self, jsonData):
        print jsonData;
        response_headers = [('Content-Type', 'application/json')];
        request = jsonData.split("=");
        print request;
        try:
            if request[0]=="stop_request":
                validatedRequest = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
                validatedRequest.setObjectProperties(request[1]);
                response = AndroclickController().searchByStop(validatedRequest.getNumber());
            elif request[0]=="line_request":
                validatedRequest = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.BUS);
                validatedRequest.setObjectProperties(request[1]);
                response = AndroclickController().searchByLine(validatedRequest.getLine());
            elif request[0]=="location_request":
                validatedRequest = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
                validatedRequest.setObjectProperties(request[1]);
                response = AndroclickController().searchByLocation(validatedRequest.getCounty(), validatedRequest.getStreet());
            else:
                responseObject = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.RESPONSE);
                responseObject.setStatus(Response.STATUS_ERROR);
                responseObject.setDescription("Bad request!");
                response = responseObject.toString();
        except ValidationException:
            responseObject = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.RESPONSE);
            responseObject.setStatus(Response.STATUS_ERROR);
            responseObject.setDescription("Bad JSON request");
            response = responseObject.toString();
        
        return response, response_headers; 
    
    def _get_page(self, environ):
        objectRequested = util.request_uri(environ).split("/")[-1];
        if(objectRequested == ""):
            objectRequested = "androclick.html";
        response, mime = WebResources.getWebResource(objectRequested);
        response_headers = [('Content-type', mime)];
        return response, response_headers;
        
