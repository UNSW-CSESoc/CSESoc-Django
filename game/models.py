from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.template.loader import render_to_string
from datetime import datetime

class Game(models.Model):
   name = models.CharField(max_length=200)
   year = models.PositiveIntegerField(unique=True)

   def __unicode__(self):
      return self.name

class Puzzle(models.Model):
   title = models.CharField(max_length=200)
   text = models.TextField()
   creation_date = models.DateTimeField(auto_now_add=True)
   update_date = models.DateTimeField(auto_now=True)
   slug = models.SlugField(help_text="slug is used for the URL. Can give small hints using it..", unique=True)
   next_puzzle = models.ForeignKey('self', blank=True, null=True)
   answer = models.CharField(max_length=1024)
   points = models.IntegerField()


   def __unicode__(self):
      return self.title

class Player(models.Model):
   username = models.CharField(max_length=30, help_text='CSE username for CSE students, student ID for others')
   email = models.EmailField(help_text='Defaults to <username>@cse.unsw.edu.au. Override for non-cse students', blank=True)

   def save(self, force_insert=False, force_update=False):
      if not self.email:
         self.email = self.username + "@cse.unsw.edu.au"
      super(Player, self).save(force_insert, force_update) # Call the "real" save() method.

   def __unicode__(self):
      return self.username

class PlayerProgress(models.Model):
   game = models.ForeignKey(Game)
   player = models.ForeignKey(Player)
   puzzle = models.ForeignKey(Puzzle)
   reached_time = models.DateTimeField()
   solved_time = models.DateTimeField(blank=True,null=True)
   def __unicode__(self):
      if self.solved_time == None:
         return unicode(self.player) + " reached " + unicode(self.puzzle) + " at " + unicode(reached_time)
      else:
         return unicode(self.player) + " solved " + unicode(self.puzzle) + " at " + unicode(solved_time)

