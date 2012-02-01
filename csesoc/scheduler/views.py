from django.forms import ModelForm
from django import forms
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from csesoc.scheduler.models import Slot, Availability
from django.conf import settings
from csesoc.forms.widgets import SliderInput
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

import datetime

class JoinForm(forms.Form):
   def __init__(self, *args, **kwargs):
      slots = kwargs.pop('slots')
      super(forms.Form, self).__init__(*args, **kwargs)
      for slot in slots:
         label = slot.title + ' ' + str(slot.start) + ' to ' + str(slot.end)
         self.fields.insert(-1, str(slot.id), forms.ChoiceField(choices=Availability.LEVEL_CHOICES, label=label, widget=SliderInput()))
   def __unicode__(self):
      return unicode(self.fields)

@login_required
def join(request):
   allslots = Slot.objects.filter(start__year=2012)
   message = "Hi " + request.user.username + ", please use the sliders to select which times are best for you from the calendar below:"
   if request.method == 'POST': # form submitted
      form = JoinForm(request.POST, slots=allslots) # form bound to POST data
      if form.is_valid():
         for field in form.fields:
            slot = Slot.objects.get(id=field)
            level = form.cleaned_data[field]
            availability = Availability.objects.get(person=request.user, slot=slot)
            availability.level = level
            availability.save()
            message = "Thanks " + request.user.username + " for submitting your preferences, you may edit them if you wish:"
      else:
         message = form._get_errors()
   else:
      initial = {}
      for slot in allslots:
         availability, created = Availability.objects.get_or_create(person=request.user, slot=slot, 
               defaults={'level': Availability.LEVEL_CHOICES[0][0]})
         initial[str(slot.id)] = availability.level
      form = JoinForm(initial=initial, slots=allslots) # unbound form

   return render_to_response('scheduler_register.html', {'message' : message, 'form' : form, 'slots' : allslots}, context_instance=RequestContext(request))

@login_required
def results(request):
   allslots = Slot.objects.filter(start__year=2012)
   slots = []
   for s in allslots:
      slots.append((s,Availability.objects.filter(slot=s).exclude(level='IM').order_by('-level'),))
   return render_to_response('weekcalendar.html', {'slots' : slots}, context_instance=RequestContext(request))

