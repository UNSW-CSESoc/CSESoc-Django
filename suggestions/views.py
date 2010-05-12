# Create your views here.
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from models import SuggestionForm
from csesoc import settings
from django.template import RequestContext


def suggest(request):
  if request.method == 'POST':
    form = SuggestionForm(request.POST)
    if form.is_valid():
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']
      sender = form.cleaned_data.get('sender', 'anon@csesoc.cse.unsw.edu.au')

      # send an email to the suggestions mailing list
      send_mail('Suggestion: %s' % subject, message, sender, ['csesoc.suggestions@cse.unsw.edu.au'])
      #send_mail('Suggestion: %s' % subject, message, sender, ['csesoc.sysadmin.head@cse.unsw.edu.au'])

      return render_to_response('thanks-suggestion.html', context_instance=RequestContext(request))
  else:
    form = SuggestionForm()

  return render_to_response('suggest.html', {'form': form}, context_instance=RequestContext(request))
