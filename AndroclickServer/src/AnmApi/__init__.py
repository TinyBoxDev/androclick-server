#!/bin/env python
#encoding:UTF-8
'''
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"
'''
class AnmException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)