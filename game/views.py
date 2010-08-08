from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from csesoc.game.models import Static
from csesoc import settings

# presently using generic views for everything. add custom views here as needed

@login_required
def game_static(request, path):
   p = get_object_or_404(Static, slug=path.replace('/','_'))
   return render_to_response('game.html', { 'object' : p }, context_instance=RequestContext(request) )

