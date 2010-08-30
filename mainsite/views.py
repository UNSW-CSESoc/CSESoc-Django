from datetime import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from csesoc.mainsite.models import Static
from csesoc import settings

# presently using generic views for everything. add custom views here as needed

def static(request, path):
   p = get_object_or_404(Static, slug=path.replace('/','_'))
   return render_to_response('static.html', { 'object' : p }, context_instance=RequestContext(request) )

def thedate(request):
   return render_to_response('thedate.html', { 'date' : datetime.now() }, context_instance=RequestContext(request) )

