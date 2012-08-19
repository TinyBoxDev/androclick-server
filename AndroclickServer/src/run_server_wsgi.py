from wsgiref.simple_server import make_server
from AndroclickCore import AndroclickCore;
from AndroclickCore.AndroclickProperties import AndroclickProperties;
import os;

androclickServer = AndroclickCore();
androclickProperties = AndroclickProperties();
port = int(os.environ.get('PORT', 5000));
httpd = make_server('0.0.0.0', port, androclickServer);
httpd.serve_forever();
