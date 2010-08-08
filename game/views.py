from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from csesoc.game.models import Puzzle
from csesoc import settings

# presently using generic views for everything. add custom views here as needed

@login_required
def game_static(request, path):
   if request.method == "POST":
      p = get_object_or_404(Puzzle, slug=path.replace('/','_'))
      answer = request.POST['answer']
      if answer == p.answer:
         # we can go to the next puzzle!
         next = p.next_puzzle
         print "YES"
         return HttpResponseRedirect('../' + next.slug)

   p = get_object_or_404(Puzzle, slug=path.replace('/','_'))
   return render_to_response('game.html', { 'object' : p, 'user': request.user }, context_instance=RequestContext(request) )
