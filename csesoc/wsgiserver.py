#!/usr/bin/python
#http://docs.python.org/library/wsgiref.html#examples
from wsgiref.simple_server import make_server

import os
import sys

path = os.path.abspath(os.path.realpath(os.path.join(os.path.dirname(__file__),'..')))
if path not in sys.path:
    sys.path.append(path)

import site
site.addsitedir('/home/www/virtualenv/lib/python2.6/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'csesoc.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
httpd = make_server('', 8001, application)
print "Serving on port 8001..."

# Serve until process is killed
httpd.serve_forever()
