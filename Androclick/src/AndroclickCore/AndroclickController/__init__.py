#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
import AndroclickCore.AndroclickObjectFactory as AndroclickObjectFactory;
from AndroclickSkeleton import AndroclickSkeleton;
from AnmApi.ANMProvider import ANMProvider;
from AnmApi.ANMPacket import HtmlResponse as AnmResponse;
from AndroclickCore.AndroclickObjectFactory.Response import Response;


class AndroclickController(AndroclickSkeleton):
    
    def searchByStop(self, number):
        print("Searching by stop...");
        stop = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
        stop.setNumber(number);
        niceResponse = self._serveRequest(stop);
        infos = niceResponse.getInfoPalina();
        
        responseMessage = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.RESPONSE);
        
        if len(infos)>1:
            responseMessage.setStatus(Response.STATUS_OK);
            responseMessage.setDescription(Response.STATUS_OK_DESC);
            responseMessage.setAdditionalInfos(infos[0:2]);
            
            busList = list();
            for bus in infos[2:]:
                busObject = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.BUS);
                busObject.setObjectPropertiesFromAnmString(bus);
                busList.append(busObject.toString());
            
            responseMessage.setObjectsArray(busList);
        else:
            responseMessage.setStatus(Response.STATUS_ERROR);
            responseMessage.setDescription(infos[0]);
        
        return responseMessage.toString();
    
    def searchByLocation(self, county, street):
        print("Searching by location...");
        stop = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
        stop.setCounty(county);
        stop.setStreet(street);
        niceResponse = self._serveRequest(stop);
        
        responseMessage = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.RESPONSE);
        try:
            infos = niceResponse.getStopList();
            responseMessage.setStatus(Response.STATUS_OK);
            responseMessage.setDescription(Response.STATUS_OK_DESC);
            
            stopList = list();
            for stop in infos:
                stopObject = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
                stopObject.setObjectPropertiesFromAnmString(stop);
                stopList.append(stopObject.toString());
            
            responseMessage.setObjectsArray(stopList);
        except:
            responseMessage.clean();
            responseMessage.setStatus(Response.STATUS_ERROR);
            responseMessage.setDescription(niceResponse.getInfoPalina()[0]);

        return responseMessage.toString();
    
    def searchByLine(self, line):
        print("Searching by line...");
        bus = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.BUS);
        bus.setLine(line);
        niceResponse = self._serveRequest(bus);
        
        responseMessage = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.RESPONSE);
        try:
            infos = niceResponse.getStopList();
            responseMessage.setStatus(Response.STATUS_OK);
            responseMessage.setDescription(Response.STATUS_OK_DESC);
            
            stopList = list();
            for stop in infos:
                stopObject = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
                stopObject.setObjectPropertiesFromAnmString(stop);
                stopList.append(stopObject.toString());
            
            responseMessage.setObjectsArray(stopList);
        except:
            responseMessage.clean();
            responseMessage.setStatus(Response.STATUS_ERROR);
            responseMessage.setDescription(niceResponse.getInfoPalina()[0]);

        return responseMessage.toString();
        
    def _serveRequest(self, androclickObject):
        anmServer = ANMProvider();
        response = anmServer.androclickFlow(androclickObject);
        print response;
        
        return AnmResponse(response);
    
if __name__ == "__main__":
    testStopString = '{"county": "", "street": "", "number": "1444"}';
    AndroclickController().searchByStop(testStopString);
    testLineString = '{"line": "R2", "time": ""}';
    AndroclickController().searchByLine(testLineString);
    testLocationString = '{"county": "NAPOLI", "street": "carlo III", "number": ""}';
    AndroclickController().searchByLocation(testLocationString);
    
