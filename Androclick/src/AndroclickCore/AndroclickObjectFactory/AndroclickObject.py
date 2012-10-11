#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
from abc import ABCMeta, abstractmethod;
from AnmApi.AnmObject import AnmObject;

class AndroclickObject(AnmObject):
    __metaclass__ = ABCMeta;
    
    @abstractmethod
    def setObjectProperties(self, bigStringOfProperties):
        pass;
    
    @abstractmethod
    def toString(self):
        pass;
    
    @abstractmethod
    def _validate(self, jsonMessage):
        pass;

class ValidationException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
