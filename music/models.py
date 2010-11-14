from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
   title = models.CharField(max_length=50, help_text='Title of song')
   artist = models.CharField(max_length=50, help_text='Artist of song')
   notes = models.TextField(max_length=200, help_text='Any notes?', blank=True, null=True)
   submitter = models.ForeignKey(User)
   submitter_hassong = models.BooleanField(help_text='Do you have this song')

   def vote(self, voter, voteAmt):
      sv = SongVote.objects.filter(song=self, voter=voter)
      if sv.count() > 0:
         sv = sv[0]
      else:
         sv = SongVote(voter=voter, song=self)
   
      sv.amount = voteAmt
      sv.save()

   def votes(self):
      try:
         from django.db.models import Sum
         return int(self.songvote_set.aggregate(Sum('amount'))['amount__sum'])
      except:
         return 0
   
   def __unicode__(self):
      return self.artist + " - " + self.title

class SongVote(models.Model):
   voter = models.ForeignKey(User)
   song = models.ForeignKey(Song)
   amount = models.IntegerField(default=0)

   def __unicode__(self):
      return str(self.amount) + " [" + self.voter.username + " for " + self.song.__unicode__() + "]"

