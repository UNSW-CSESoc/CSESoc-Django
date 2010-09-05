from django.shortcuts import render_to_response
from django.template import RequestContext
from csesoc.sponsors.models import Sponsor
from csesoc import settings

def sponsors(request):
  return render_to_response('sponsor.html', {'allSponsors' : Sponsor.objects.order_by('rank')}, context_instance = RequestContext(request))
