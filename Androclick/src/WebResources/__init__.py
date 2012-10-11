#!/bin/env python
#encoding:UTF-8
'''
__init__.py
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"

How this great application provides all the stupid things you want? Simply thanks to me :)
I get your request for a stupid object, I parse it in a almost-stupid way, and look for the resource.
Be carefully: if you submit me a wrong request.. I will take you around!
'''
from AndroclickCore.AndroclickProperties import AndroclickProperties;
import os;

# This is the error page provided if I don't like your request
_errorPage = """
<html>
<head>
<title>you are so stupid!</title>
</head>
<body>
<h1 align="center">ok, ok, you think you are smarter than me??<br><b>What a n00b!</b></h1><br><br>
<p align="center">
<img width="50%" src="genius-meme.png">
</p>
</body>
</html>    
"""

def getWebResource(objectName):
    ''' A web resource factory.. Yes, tell me what you need and I will find for you! '''
    objectName = os.path.join(AndroclickProperties().getRootFolder(), "StaticObjects", objectName);
    print ("Requested file ", objectName);
    objectLoaded=None;
    mime=None;
    # Sooooo what do you want?
    try:
        if(objectName.endswith('html')): # do you want an html page?
            mime="text/html";
            objectLoaded=open(objectName).read().encode('utf8');
        elif(objectName.endswith('png')): # do you want a png image?
            mime="image/png";
            objectLoaded=open(objectName, "rb").read();
        elif(objectName.endswith('jpg')): # do you want a jpeg image?
            mime="image/jpeg";
            objectLoaded=open(objectName, "rb").read();
        elif(objectName.endswith('css')): # do you want a css file?
            mime="text/css"
            objectLoaded=open(objectName).read().encode('utf8');
        elif(objectName.endswith('ico')): # do you want an ico file?
            mime="image/vnd.microsoft.icon";
            objectLoaded=open(objectName, "rb").read();
        else: # oh God... f**k you and your stupid request!
            raise Exception;
    except:
        mime="text/html";
        objectLoaded=_errorPage.encode('utf8');

    return objectLoaded, mime;