import os
import sys

path = os.path.abspath(os.path.realpath(os.path.join(os.path.dirname(__file__),'..')))
if path not in sys.path:
    sys.path.append(path)

import site
site.addsitedir('/home/www/virtualenv/lib/python2.6/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'csesoc.production_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
"""
import posixpath
def application(environ, start_response):
    # Wrapper to set SCRIPT_NAME to actual mount point.
    environ['SCRIPT_NAME'] = posixpath.dirname(environ['SCRIPT_NAME'])
    if environ['SCRIPT_NAME'] == '/':
        environ['SCRIPT_NAME'] = ''
    import pprint
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield pprint.pformat(environ)
#    return _application(environ, start_response)
"""
