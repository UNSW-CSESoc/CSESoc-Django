#!/usr/bin/python
import sys, os

# Add a custom Python path.
# Why can't this use relative paths?
# Or system python?
# sys.path.insert(0, "/home/csesoc/internal_site/django1.1/lib/python2.5/site-packages")
sys.path.insert(0, "/home/www/csesoc-django/current")

# Switch to the directory of your project. (Needed for FilePathField)
os.chdir("/home/www/csesoc-django/current")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "csesoc.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
