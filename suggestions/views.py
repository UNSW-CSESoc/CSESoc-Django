# Create your views here.
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from models import Suggestion
from csesoc import settings
from django.template import RequestContext
from django.http import Http404
from django import forms

def comments(request, comment):
   raise Http404

def suggest(request):
  if request.method == 'POST':
    form = SuggestionForm(request.POST)
    if form.is_valid():
      clean_subject = form.cleaned_data['subject']
      clean_message = form.cleaned_data['message']
      clean_sender = form.cleaned_data.get('sender', 'anon@csesoc.cse.unsw.edu.au')

      suggestion = Suggestion(subject=clean_subject, message=clean_message, sender=clean_sender)
      suggestion.save()

      # send an email to the suggestions mailing list
      #send_mail('Suggestion: %s' % clean_subject, clean_message, clean_sender, ['csesoc.suggestions@cse.unsw.edu.au'])
      #send_mail('Suggestion: %s' % subject, message, sender, ['csesoc.sysadmin.head@cse.unsw.edu.au'])

      return render_to_response('thanks-suggestion.html', context_instance=RequestContext(request))
  else:
    form = SuggestionForm()

  return render_to_response('suggest.html', context_instance=RequestContext(request, {'form': form}))

class SuggestionForm(forms.Form):
   subject = forms.CharField(max_length=100)
   message = forms.CharField(widget=forms.Textarea(), initial="Replace with your suggestion.")
   sender = forms.EmailField(required=False)
