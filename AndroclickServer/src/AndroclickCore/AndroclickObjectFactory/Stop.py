#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
from AndroclickObject import AndroclickObject;
from AndroclickObject import ValidationException;
import json;
from AnmApi import ANMPacket;
import re;

# Protocol constraints
NUMBER = 'number';
COUNTY = 'county';
STREET = 'street';
COUNTY_DEFAULT = 'NAPOLI';

class Stop(AndroclickObject):
    _number = '';
    _county = '';
    _street = '';
    
    def getNumber(self):
        return self._number;
    
    def setNumber(self, stopNumber):
        self._number = stopNumber;
    
    def getCounty(self):
        return self._county;
    
    def setCounty(self, currentCounty):
        self._county = currentCounty.upper();
        
    def getStreet(self):
        return self._street;
    
    def setStreet(self, currentStreet):
        self._street = currentStreet;
    
    def setObjectProperties(self, bigStringOfProperties):
        receivedData = json.loads(bigStringOfProperties);
        self._validate(receivedData);
        self._number = receivedData[NUMBER];
        self._county = receivedData[COUNTY].upper();
        self._street = receivedData[STREET];
    
    def toString(self):
        dataList = { NUMBER : self._number, COUNTY : self._county, STREET : self._street };
        return json.dumps(dataList);
    
    def setObjectPropertiesFromAnmString(self, bigStringOfProperties):
        infoArray = bigStringOfProperties.split('-');
        self._number = infoArray[0];
        self._county = re.findall(r'\w+', infoArray[1])[0];
        self._street = infoArray[1].split(self._county + " ")[1];
            
    def toAnmString(self):
        if self._county=='':
            self._county=COUNTY_DEFAULT;
        return ANMPacket.genPacket(self._eventValidation, self._viewState, self._number, self._street, self._county, '');
    
    def _validate(self, jsonMessage):
        if (jsonMessage[NUMBER]!='' and jsonMessage[COUNTY]=='' and jsonMessage[STREET]=='') or (jsonMessage[NUMBER]=='' and jsonMessage[COUNTY]!='' and jsonMessage[STREET]!=''):
            print("Message received is ok!");
        else:
            raise ValidationException("The json request is not well formed: " + str(jsonMessage));

# Test function :)
if __name__ == '__main__':
    c = Stop();
    c.setNumber(9844);
    c.setStreet('ciaoooo');
    c.setCounty('casoria');
    s = c.toString();
    print(s);
    c.setCounty('Mapoli');
    c.setStreet('coglia');
    c.setNumber(0000);
    c.setObjectProperties(c.toString());
    print(c.toString());
    stringWithInfos = u'1444- NAPOLI PIAZZA GARIBALDI Stazione Centrale';
    c.setObjectPropertiesFromAnmString(stringWithInfos);
    print(c.toString());
