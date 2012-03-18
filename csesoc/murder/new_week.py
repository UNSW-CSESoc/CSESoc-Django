#!/usr/bin/python
# Begin dirty path hack
import os
from os import path
import sys
baseDir = path.abspath(path.split(sys.argv[0])[0] + '/../..')
print baseDir
sys.path.insert(0, baseDir)
# end dirty path hack
from csesoc import set_path
set_path.update_path()

from django.core.management import setup_environ
from datetime import date, datetime, timedelta
from django.conf import settings

setup_environ(settings)

from csesoc.murder.models import *

# These change per session
gameName = '2012 Session 1'

# start_day <= today <= last_day
currentGames = Game.objects.filter(start_day__lte=date.today()).filter(last_day__gte=date.today())
if currentGames.count() > 0:
  # there should only be one game but get game 0 just in case
  currentGame = currentGames[0]
  difference = date.today() - currentGame.start_day
  roundname = "Week %d" % (difference.days / 7)

  # Set the round start and end dates
  roundlength = timedelta(days=7) - timedelta(minutes=20)
  startdate = datetime.now()
  enddate = startdate + roundlength

  r = Round(name=roundname, start=startdate, end=enddate, game=currentGame)
  r.save()

