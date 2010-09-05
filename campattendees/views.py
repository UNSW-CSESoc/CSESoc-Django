from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from models import Application
from csesoc import settings
from django.template import RequestContext
import datetime
import urllib
from csesoc import passwd_data

class ApplicationForm(ModelForm):
   class Meta:
      model = Application
      exclude = ('medical_form','payment_status',)

def signup(request):
   this_year = datetime.date.today().year
   if request.method == 'POST': # form submitted
      appl = Application(year=this_year)
      form = ApplicationForm(request.POST, instance=appl) # form bound to POST data
      if form.is_valid():
         form.save() # create new Application instance
         return render_to_response('thanks-signup.html', context_instance=RequestContext(request))
   else:
      username = ''
      if request.COOKIES.has_key('cseauth'):
         uname = request.COOKIES['cseauth']
         uname = urllib.unquote(uname)
         uname = uname.decode('iso-8859-1')
         db = MySQLdb.connect(db='cse_auth', user=passwd_data.DB_USERNAME, passwd=passwd_data.DB_PASSWORD)
         c = db.cursor()
         c.execute('select `user` from `users` where `cookie` = %s;', (uname,))
         
         row = c.fetchone()
         if row and row[0]:
            username = row[0]

      appl = Application(year=this_year, cse_username = username)
      form = ApplicationForm(instance=appl) # unbound form

   return render_to_response('signup.html', {'form' : form}, context_instance=RequestContext(request))

