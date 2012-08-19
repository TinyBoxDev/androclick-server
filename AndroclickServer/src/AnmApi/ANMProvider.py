#!/bin/env python
#encoding:UTF-8
'''
ANMProvider.py
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
import urllib2;
from AnmApi import AnmException;
import AndroclickCore.AndroclickObjectFactory as AndroclickObjectFactory;

SERVER_URL = "http://www.anm.it/Default.aspx";
USER_AGENT_KEY = 'User-agent';
USER_AGENT_VALUE = 'Androclick Smart Server';
COOKIE_KEY = 'Cookie';

class ANMProvider(object):
    
    def androclickFlow(self, androclickObject):
        # Getting initial informations
        firstStep = self._sendRequest();
        
        cookie = firstStep.info().get("Set-Cookie").split(";")[0];
        print "Received cookie: " + cookie;
        htmlPage = firstStep.read();
        print "Received data: " + htmlPage;
        
        androclickObject.setRequestProperties(htmlPage);
        completeRequest = androclickObject.toAnmString();
        print("Sending request: " + completeRequest + "\n");
        
        finalStep = self._sendRequest(completeRequest, cookie);
        finalResponse = finalStep.read();
        print("Ultimate reply: " + finalResponse)
        
        return finalResponse;
    
    def _sendRequest(self, requestData=None, currentCookie=None):
        connection = urllib2.build_opener();
        
        connection.addheaders = [(USER_AGENT_KEY, USER_AGENT_VALUE)];
        
        if currentCookie != None:
            connection.addheaders.extend([(COOKIE_KEY, currentCookie)]);
        
        try:
            response = connection.open(SERVER_URL, requestData);
        except urllib2.HTTPError as httpException:
            raise AnmException("ANMProvider.py - Remote server error: " + str(httpException.code));# + " " + httpException.reason);
        except Exception as generalException:
            raise AnmException("ANMProvider.py - Local error: " + str(generalException.reason));
        
        connection.close();
        
        return response;
                
if __name__ == "__main__":
    bus = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.BUS);
    bus.setLine('r2');
    requestedObject = ANMProvider().androclickFlow(bus);
    print(requestedObject);
    stop = AndroclickObjectFactory.getAndroclickObject(AndroclickObjectFactory.STOP);
    stop.setNumber('3352');
    requestedObject = ANMProvider().androclickFlow(stop);
    print(requestedObject);

            
