from django.forms import ModelForm
from django import forms
from django.shortcuts import render_to_response
from models import AwkwardQuestion
from models import Application
from csesoc import settings
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

class ApplicationForm(ModelForm):
   q9question = forms.ModelChoiceField(queryset=AwkwardQuestion.objects.all(),
                                       widget=forms.HiddenInput)
   def setQ9(self, q9question):
       self.fields['q9'] = forms.CharField(widget=forms.Textarea,
                                           help_text=str(q9question),
                                           #dodgy hack for poor design decision
                                           label="Q6")

   class Meta:
      model = Application
      # to use if we upgrade django
      #http://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-field-types-or-widgets
      #widgets = {'q9question': forms.HiddenInput}
      exclude = ( 'cse_username', 'q5', 'q6', 'q7')

@login_required
def apply(request):
   year = (datetime.date.today() + timedelta(weeks=21)).year
   if request.method == 'POST': # form submitted
      apps = Application.objects.filter(cse_username=request.user.username, year=year)
      if len(apps) == 0:
        appl = Application(year=year, cse_username=request.user.username)
      else:
        appl = apps[0]
      form = ApplicationForm(request.POST, instance=appl) # form bound to POST data
      form.setQ9(AwkwardQuestion.objects.get(id=int(request.POST['q9question'])))
      if form.is_valid():
         form.save() # create new Application instance
         return render_to_response('thanks.html', context_instance=RequestContext(request))
   else:
      q9question = AwkwardQuestion.objects.order_by('?')[0]
      apps = Application.objects.filter(cse_username=request.user.username).order_by('-year')
      if len(apps) == 0:
        most_recent_app = Application(cse_username=request.user.username)
        initial = {'q9question': q9question.id}
      else:
        most_recent_app = apps[0]
        if most_recent_app.year != year:
          initial = {'q9question': q9question.id, 'q9': ''}
        else:
          initial = {}
        most_recent_app.year = year
      form = ApplicationForm(instance=most_recent_app, initial=initial) # unbound form
      form.setQ9(q9question)

   return render_to_response('apply.html', {'form' : form}, context_instance=RequestContext(request))
