#!/bin/env python
#encoding:UTF-8
'''
run_server.py
Created on Jun 24, 2012

@author: "helloIAmPau - Pasquale Boemio <boemianrapsodi[at]gmail.com>"

Welcome to Androclick server!
This is the script that fulfills your inner desires... You have only to run this!
As you can see, it uses fapws-wsgi interface that has been compiled for "littlemonkey" remote machine and has been copied into the libs folder.
If you want to run Androclick Server on another machine, you have to recompile fapws-wsgi for the destination machine. It is because it was written 
C language...
Dropping these bad things, this script creates a new server application, create a new AndroclickCore object, read the server properties
from the configuration file in the folder /etc e run everything..

Don't forget to configure properly the PYTHONPATH with the absolute path of the folders src and libs!  
'''
import fapws._evwsgi as evwsgi;
from fapws import base;
from AndroclickCore import AndroclickCore;
from AndroclickCore.AndroclickProperties import AndroclickProperties;

if __name__ == '__main__':
    ''' Where everything begins '''
    androclickServer = AndroclickCore(); # Hi! my name is Androclick Server :)  
    androclickProperties = AndroclickProperties(); # ...and I'm the smarter way to get usefull informations.
    # some things that we don't cares
    evwsgi.start(androclickProperties.getServerAddress(), str(androclickProperties.getPortNumber()));
    evwsgi.set_base_module(base);
    evwsgi.wsgi_cb(("/", androclickServer));
    evwsgi.run();
