from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from csesoc.game.models import *
from csesoc import settings
import datetime
from django.db.models import Sum

# presently using generic views for everything. add custom views here as needed

def get_player(username):
   p = Player.objects.filter(username=username)
   if len(p) > 0:
      return p[0]
   else:
      p = Player()
      p.username = username
      p.save()
      return p

def get_progress(puzzle, username):
   player = get_player(username)
   game = get_object_or_404(Game, year = datetime.datetime.now().year)

   progress = PlayerProgress.objects.filter(player=player, puzzle=puzzle, game=game)
   if len(progress) > 0:
      return progress[0]
   else:
      progress = PlayerProgress()
      progress.game = game
      progress.puzzle = puzzle
      progress.player = player
      progress.reached_time = datetime.datetime.now()
      progress.save()

def solved_puzzle(puzzle, username):
   progress = get_progress(puzzle, username)
   progress.solved_time = datetime.datetime.now()
   progress.save()

def reached_puzzle(puzzle, username):
   # automatically creates it if required
   progress = get_progress(puzzle, username)

def made_attempt(puzzle, username, value):
   progress = get_progress(puzzle, username)

   attempt = PlayerAttempt()
   attempt.progress = progress
   attempt.attempt_time = datetime.datetime.now()
   attempt.attempt = value
   attempt.save()

def game_scores(request, year):
   if year == "":
      year = datetime.datetime.now().year
   else:
      year = int(year)

   # the magical line that calculates the scores
   scores = PlayerProgress.objects.filter(game__year__startswith=2010).filter(solved_time__isnull=False).values('player__username').annotate(Sum('puzzle__points')).order_by('-puzzle__points__sum')
   return render_to_response('scores.html', {'scores': scores})


@login_required
def game_static(request, path):
   if request.method == "POST":
      p = get_object_or_404(Puzzle, slug=path.replace('/','_'))
      answer = request.POST['answer']
      made_attempt(p, request.user.username, answer)
      if answer == p.answer and p.next_puzzle != None:
         # we can go to the next puzzle!
         next = p.next_puzzle

         solved_puzzle(p, request.user.username)

         return HttpResponseRedirect(next.slug)

   p = get_object_or_404(Puzzle, slug=path.replace('/','_'))
   reached_puzzle(p, request.user.username)
   return render_to_response('game.html', { 'object' : p, 'user': request.user, 'showanswer' : (p.next_puzzle != None) }, context_instance=RequestContext(request) )
