from csesoc import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def sponsors(request):
  return render_to_response('sponsor.html', context_instance=RequestContext(request))
