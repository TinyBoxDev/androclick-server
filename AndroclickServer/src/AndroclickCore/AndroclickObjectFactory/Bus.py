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
TIME = 'time';
LINE = 'line';

class Bus(AndroclickObject):
    _time = None;
    _line = None;
    
    def getTime(self):
        return self._time;
    
    def setTime(self, currentTime):
        self._time = currentTime;
    
    def getLine(self):
        return self._line;
    
    def setLine(self, currentLine):
        self._line = currentLine;
        
    def setObjectProperties(self, bigStringOfProperties):
        receivedData = json.loads(bigStringOfProperties);
        self._validate(receivedData);
        self._time = receivedData[TIME];
        self._line = receivedData[LINE];
            
    
    def toString(self):
        dataList = { TIME : self._time, LINE : self._line };
        return json.dumps(dataList);
    
    def setObjectPropertiesFromAnmString(self, bigStringOfProperties):
        infoArray = re.findall(r'\w+', bigStringOfProperties);
        self._line = infoArray[1];
        self._time = infoArray[2] + ":" + infoArray[3];
            
    def toAnmString(self):
        return ANMPacket.genPacket(self._eventValidation, self._viewState, '', '', 'NAPOLI', self._line);
    
    def _validate(self, jsonMessage):
        if jsonMessage[TIME]=='' and jsonMessage[LINE]!='':
            print("Message received is ok!");
        else:
            raise ValidationException("The json request is not well formed: " + str(jsonMessage));

# Test function :)
if __name__ == '__main__':
    c = Bus();
    c.setTime('ddd');
    c.setLine('ffr');
    s = c.toString();
    print(s);
    c.setTime('cacchio');
    c.setLine('cacchio');
    c.setObjectProperties(c.toString());
    print(c.toString());
    c.setEventArgument("eventArgument");
    c.setViewState("viewState");
    c.setEventValidation("eventValidation");
    print(c.toAnmString());
    stringWithInfos = u'Linea 181    09:26\n';
    c.setObjectPropertiesFromAnmString(stringWithInfos);
    print(c.getLine());
    print(c.getTime());
