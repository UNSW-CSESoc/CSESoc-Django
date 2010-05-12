from django.shortcuts import render_to_response
from csesoc.murder.models import *
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import logout
from django import forms
from django.template import RequestContext

def gamelist(request):
   return render_to_response('games.html', RequestContext(request, { 'games': Game.objects.order_by('id') }))

def index(request, game):
   try:
      return render_to_response('index.html', RequestContext(request, { 'game': Game.objects.get(slug=game) }))
   except Game.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))

def scoreboard(request, game):
   try:
      c = defaultdict(int)
      gameo = Game.objects.get(slug=game)
      total = 0
      for round in gameo.round_set.all():
         for kill in round.kill_set.all():
            c[kill.killer.username] += 1
            total += 1
      counts = sorted(c.iteritems(), key = lambda (k,v):(v,k), reverse=True)
      return render_to_response('scoreboard.html', RequestContext(request, { 'game': gameo, 'counts': counts, 'total': total }))
   except Game.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))

def newkills(request, game):
   try:
      c = defaultdict(int)
      gameo = Game.objects.get(slug=game)
      kills = gameo.round_set.get(start__lt=datetime.now, end__gt=datetime.now()).kill_set.order_by('-datetime')
      return render_to_response('newkills.html', RequestContext(request, { 'game': gameo, 'kills': kills }))

   except Round.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'No Current Round. Go Away!' }))
   except Game.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))

def roundkills(request, game, roundid):
   return render_to_response('basic.html', RequestContext(request, { 'title':'roundkills' }))

# form to kill victim
class KillForm(forms.Form):
   password = forms.CharField(max_length=100)

@login_required
def myvictim(request, game):

   try:
      current_round = Game.objects.get(slug=game).round_set.get(start__lt=datetime.now, end__gt=datetime.now())

      rp = current_round.roundplayer_set.get(player=Player.objects.get(username=request.user.username))   

      if not rp.alive:
         return render_to_response('basic.html', RequestContext(request, { 'title':'You are DEAD. See you next week!' }))

      flash = ''
      if request.method == 'POST':
         form = KillForm(request.POST)
         if form.is_valid():
            password = form.cleaned_data['password']
            if password == current_round.roundplayer_set.get(player=rp.currentvictim).password.text:
               k = Kill(round=current_round, killer=rp.player)
               k.save()
               flash = 'Good Kill!'
               rp = current_round.roundplayer_set.get(player=Player.objects.get(username=request.user.username))   
            else:
               flash = 'Wrong Password!'
      else:
         form = KillForm()

      return render_to_response('myvictim.html', 
            RequestContext(request, {'victim':rp.currentvictim, 'gameslug':game, 'flash':flash, 'form':form}))

   except Round.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'No Current Round. Go Away!' }))
   except Game.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))
   except RoundPlayer.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'You are not registered in this round. Go Away!' }))
   except Player.DoesNotExist:
      return render_to_response('basic.html', RequestContext(request, { 'title':'You are not registered in this game. Go Away!' }))

def logout_game(request, game):
   logout(request)
   return index(request, game)

