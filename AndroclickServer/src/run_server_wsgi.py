from wsgiref.simple_server import make_server
from AndroclickCore import AndroclickCore;
from AndroclickCore.AndroclickProperties import AndroclickProperties;

androclickServer = AndroclickCore();
androclickProperties = AndroclickProperties();
httpd = make_server('0.0.0.0', 50233, androclickServer);
httpd.serve_forever();
