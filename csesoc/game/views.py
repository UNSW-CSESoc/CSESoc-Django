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
   if progress.solved_time == None:
      progress.solved_time = datetime.datetime.now()
      progress.save()

# check whether what they entered is the answer
def check_solved(puzzle, username, answer):
   # exact matches are always good
   if answer.lower() == puzzle.answer.lower():
      return True
   elif ";" in puzzle.answer:
      answerParts = answer.split(" ")
      ansParts = puzzle.answer.split(";")

      # we should not have way more tems in answerParts than puzzle answer parts
      if len(answerParts) > len(ansParts) + 5:
         return False

      # check that all the parts are in there
      for ans in ansParts:
         if ans not in answerParts:
            return False

      return True
   else:
      return False


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

#TODO: check that the user is logged in and player.isAdmin()
# requires the player.isAdmin() function to be written first

# returns "th", where "th" can be "st", "nd", "rd", or "th"
def ordinal(n):
    return dict([(x,'th') for x in range(10,20)]).get(n%100,{1:'st',2:'nd',3:'rd'}.get(n%10,'th'))

def get_player_scores(request, year):
   return PlayerProgress.objects.filter(game__year__startswith=2010).filter(solved_time__isnull=False).values('player__username').annotate(Sum('puzzle__points')).order_by('-puzzle__points__sum')

def game_scores(request, year):
   if year == "":
      year = datetime.datetime.now().year
   else:
      year = int(year)

   # the magical line that calculates the scores
   scores = get_player_scores(request, year)
   return render_to_response('scores.html', {'scores': scores})

@login_required
def game_static_latest(request):
    p = get_player(request.user.username)
    last_puzzle = p.upto()
    return HttpResponseRedirect(last_puzzle.slug) 


@login_required
def game_static(request, path):
   if request.method == "POST":
      p = get_object_or_404(Puzzle, slug=path.replace('/','_'))
      answer = request.POST['answer']
      made_attempt(p, request.user.username, answer)
      if check_solved(p, request.user.username, answer) and p.next_puzzle != None:
         # we can go to the next puzzle!
         next = p.next_puzzle

         solved_puzzle(p, request.user.username)

         return HttpResponseRedirect(next.slug)

   p = get_object_or_404(Puzzle, slug=path.replace('/','_'))
   reached_puzzle(p, request.user.username)
   
   # get the player's rank
   player_rank = get_player(request.user.username).rank()
   rank = "You are "
   if player_rank['tied']:
      rank += "tied in"
   else:
      rank += "ranked"
   rank += " "+str(player_rank['rank'])+ordinal(player_rank['rank'])+" place!"

   return render_to_response('game.html', { 'object' : p, 'user': request.user, 'showanswer' : (p.next_puzzle != None), 'rank' : rank }, context_instance=RequestContext(request) )
