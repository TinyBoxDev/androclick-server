#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''

class AndroclickSkeleton():
    
    def searchByStop(self, number):
        raise NotImplementedError;
    
    def searchByLocation(self, county, street):
        raise NotImplementedError;
    
    def searchByLine(self, line):
        raise NotImplementedError;
