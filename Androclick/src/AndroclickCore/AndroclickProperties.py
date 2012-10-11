#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
import os;
import ConfigParser as configparser;
#import configparser;

class AndroclickProperties(object):
    _configurationFile = None;
    _myself = None;
    
    def __new__(cls, *args, **kwargs):
        if cls._myself == None:
            cls._myself = super(AndroclickProperties, cls).__new__(cls, *args, **kwargs);
            cls._myself._loadConfigurationFile();
        
        return cls._myself;
    
    def getRootFolder(self):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."));
    
    def getPortNumber(self):
        return int(self._configurationFile.get("server", "port"));
    
    def getServerAddress(self):
        return self._configurationFile.get("server", "address");
    
    def _loadConfigurationFile(self):
        configurationFilePath = os.path.join(self.getRootFolder(), "etc", "androclick.conf");
        print ("Reading configuration from file ", configurationFilePath);
        self._configurationFile = configparser.RawConfigParser();
        self._configurationFile.read(configurationFilePath);

