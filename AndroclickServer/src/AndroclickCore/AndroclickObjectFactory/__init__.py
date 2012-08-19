#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''

from Bus import Bus;
from Stop import Stop;
from Response import Response

BUS = 0;
STOP = 1;
RESPONSE = 2;
    
def getAndroclickObject(objectType):
    if objectType == BUS:
        return Bus();
    elif objectType == STOP:
        return Stop();
    elif objectType == RESPONSE:
        return Response();
    else:
        print("Invalid object type");
