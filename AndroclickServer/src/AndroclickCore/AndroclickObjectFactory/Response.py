'''
Created on Jun 26, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
import json;

    
STATUS_KEY = 'status';
DESCRIPTION_KEY = 'description';
OBJECTS_ARRAY_KEY = 'androclick_objects';
ADDITIONAL_INFOS_KEY = 'additional_infos';

class Response(object):

    STATUS_OK = 0;
    STATUS_ERROR = 1;
    STATUS_OK_DESC = 'ok';

    _status = None;
    _description = None;
    _objectsArray = None;
    _additionalInfos = None;
    
    def clean(self):
        self._status = None;
        self._description = None;
        self._objectsArray = None;
        self._additionalInfos = None;
    
    def setStatus(self, status):
        self._status = status;
        
    def getStatus(self):
        return self._status;
    
    def setDescription(self, description):
        self._description = description;
        
    def getDescription(self):
        return self._description;
    
    def setObjectsArray(self, array):
        self._objectsArray = array;
        
    def getObjectsArray(self):
        return self._objectsArray;
    
    def setAdditionalInfos(self, additionalInfos):
        self._additionalInfos = additionalInfos;
        
    def getAdditionalInfos(self):
        return self._additionalInfos;
    
    def setObjectProperties(self, bigStringOfProperties):
        receivedData = json.loads(bigStringOfProperties);
        self._validate(receivedData);
        self._status = receivedData[STATUS_KEY];
        self._description = receivedData[DESCRIPTION_KEY];
        self._objectsArray = receivedData[OBJECTS_ARRAY_KEY];
    
    def toString(self):
        jsonResponse = {
                        STATUS_KEY : self._status,
                        DESCRIPTION_KEY : self._description
                        };
        if self._objectsArray!=None:
            jsonResponse.update({OBJECTS_ARRAY_KEY : self._objectsArray});
        if self._additionalInfos!=None:
            jsonResponse.update({ADDITIONAL_INFOS_KEY : self._additionalInfos});
        
        return json.dumps(jsonResponse);
        
    
    def _validate(self, jsonMessage):
        pass;