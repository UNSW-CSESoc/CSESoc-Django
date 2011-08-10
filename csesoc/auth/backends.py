from django.contrib.auth.backends import ModelBackend 
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import admin
from csesoc import settings
from django.template import RequestContext
from csesoc import csesoc_settings
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from csesoc import admin_urls
from django.core.urlresolvers import get_resolver

class CSEBackend(ModelBackend):
   def authenticate(self, token=None):
        import urllib
        from django.contrib.auth.models import User
        
        #Check if we have turned off login (for dev work)
        if csesoc_settings.ADMIN_NO_LOGIN == False:
            # Check the token and return a User.
            token = urllib.unquote(token)
            token = token.decode('iso-8859-1')
            import MySQLdb
            db = MySQLdb.connect(db='cse_auth', user=csesoc_settings.DB_USERNAME, passwd=csesoc_settings.DB_PASSWORD)
            c = db.cursor()
            c.execute('select `user` from `users` where `cookie` = %s;', (token,))

            #If cookie already exists in DB, return the User
            row = c.fetchone()
            if row and row[0]:
              username = row[0]
            #Otherwise user has not actually logged in, so return None 
            else:
              return None

            user, created = User.objects.get_or_create(username=username, 
                   defaults={'password' : 'get from cse',
                             'is_staff' : False,
                             'is_superuser' : False})
            return user
        #If login is turned off, just create a test_admin user
        else:
            user, created = User.objects.get_or_create(username="test_admin",
                   defaults={'password' : 'get from cse',
                             'is_staff' : True,
                             'is_superuser' : True})
            return user

def cse_login(request, next=None):
   from django.conf import settings
   if "CSE" not in settings.AUTHENTICATION_BACKENDS[0]:
       return login(request, next)

   #Check if already authenticated
   if not request.user.is_authenticated():
      user = None
      #If no login is turned on, then we don't need to pass in token
      if csesoc_settings.ADMIN_NO_LOGIN:
         user = authenticate()
      #If our cookie indicates we have already logged in before, just use the same token
      elif request.COOKIES.has_key('cseauth'):
         user = authenticate(token=request.COOKIES['cseauth'])

      #If we've managed to get a user, then log in...
      if user is not None:
         if user.is_active:
            login(request, user)
         else:
            return render_to_response('go_away.html', context_instance=RequestContext(request))
      #...otherwise use the cse_auth login to set up DB and cookie
      else:
         return HttpResponseRedirect('https://cgi.cse.unsw.edu.au/~csesoc/services/cse_auth/?redirectTo=' + request.build_absolute_uri())

   #Now just pass move onto the page the user was actually trying to get to
   if request.GET.has_key('next'):
      return HttpResponseRedirect(request.GET['next'])
   else:
      return HttpResponseRedirect(next)

def admin_wrapper(request):
   #Authenticate user if not already done
   from django.conf import settings
   if "CSE" in settings.AUTHENTICATION_BACKENDS[0]:
      if not request.user.is_authenticated():
         print "Not authenticated"
         return cse_login(request, request.path)
   
   #If authenticated, then resolve url to get view and call it
   admin_url_resolver = get_resolver(admin_urls)
   func, args, kwargs = admin_url_resolver.resolve(request.path)
   return func(request, *args, **kwargs)
