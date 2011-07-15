import os
import sys

path = '/home/www/csesoc-django/current/'
if path not in sys.path:
    sys.path.append(path)

# Switch to the directory of your project. (Needed for FilePathField)
os.chdir(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'csesoc.settings'

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
