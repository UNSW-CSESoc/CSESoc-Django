from django.contrib.auth.backends import ModelBackend 
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import admin
from csesoc import settings
from django.template import RequestContext
from csesoc import passwd_data

class CSEBackend(ModelBackend):
   def authenticate(self, token=None):
        import MySQLdb
        import urllib
        from django.contrib.auth.models import User
        if passwd_data.ADMIN_NO_LOGIN == False:
            token = urllib.unquote(token)
            token = token.decode('iso-8859-1')
            # Check the token and return a User.
            db = MySQLdb.connect(db='cse_auth', user=passwd_data.DB_USERNAME, passwd=passwd_data.DB_PASSWORD)
            c = db.cursor()
            c.execute('select `user` from `users` where `cookie` = %s;', (token,))

            row = c.fetchone()
            if row and row[0]:
              username = row[0]
            else:
              return None
            user, created = User.objects.get_or_create(username=username, 
                   defaults={'password' : 'get from cse',
                             'is_staff' : False,
                             'is_superuser' : False})
            return user
        else:
            user, created = User.objects.get_or_create(username="test_admin",
                   defaults={'password' : 'get from cse',
                             'is_staff' : True,
                             'is_superuser' : True})
            return user

def cse_login(request, next=None):
   if not request.user.is_authenticated():
      user = None
      if request.COOKIES.has_key('cseauth'):
         user = authenticate(token=request.COOKIES['cseauth'])
      if passwd_data.ADMIN_NO_LOGIN:
          user = authenticate()
      if user is not None:
         if user.is_active:
            login(request, user)
         else:
            return render_to_response('go_away.html', context_instance=RequestContext(request))
      else:
         return HttpResponseRedirect('https://cgi.cse.unsw.edu.au/~csesoc/services/cse_auth/?redirectTo=' + request.build_absolute_uri())
   if request.GET.has_key('next'):
      return HttpResponseRedirect(request.GET['next'])
   else:
      return HttpResponseRedirect(next)

def admin_wrapper(request, url):
   if not request.user.is_authenticated():
      return cse_login(request, url)
   return admin.site.root(request, url)

