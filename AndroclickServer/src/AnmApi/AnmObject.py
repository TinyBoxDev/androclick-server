#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
from abc import ABCMeta, abstractmethod;
from ANMPacket import HtmlResponse as ANMResponse;

class AnmObject(object):
    __metaclass__ = ABCMeta;
    
    _eventValidation = None;
    _eventArgument = None;
    _viewState = None;
    _eventTarget = None;
    
    @abstractmethod
    def setObjectPropertiesFromAnmString(self, bigStringOfProperties):
        pass;
    
    @abstractmethod
    def toAnmString(self):
        pass;
    
    def setRequestProperties(self, bigStringOfProperties):
        objectFillWithProperties = ANMResponse(bigStringOfProperties);
        self._eventValidation = objectFillWithProperties.getEventValidation();
        self._viewState = objectFillWithProperties.getViewState();
            
    def setEventValidation(self, eventValidation):
        self._eventValidation = eventValidation;
        
    def getEventValidation(self):
        return self._eventValidation;
    
    def setEventArgument(self, eventArgument):
        self._eventArgument = eventArgument;
        
    def getEventArgument(self):
        return self._eventArgument;
    
    def setViewState(self, viewState):
        self._viewState = viewState;
        
    def getViewState(self):
        return self._viewState;
    
    def setEventTarget(self, eventTarget):
        self._eventTarget = eventTarget;
        
    def getEventTarget(self):
        return self._eventTarget;
