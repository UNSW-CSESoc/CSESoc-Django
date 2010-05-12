from django.db import models
from django.contrib.auth.models import User

class Slot(models.Model):
   title = models.CharField(max_length=200)
   start = models.DateTimeField()
   end = models.DateTimeField()
   def __unicode__(self):
      return self.title + ' ' + unicode(self.start) + ' to ' + unicode(self.end)
   class Meta:
      ordering = ('start',)

class Availability(models.Model):
   person = models.ForeignKey(User)
   slot = models.ForeignKey(Slot)
   LEVEL_CHOICES = (
         ('IM', 'Impossible'),
         ('DL', 'Dislike'),
         ('PO', 'Possible'),
         ('PR', 'Preferred'),
         )
   LEVEL_DICT = {}
   for code, full in LEVEL_CHOICES:
      LEVEL_DICT[code] = full
   level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
   def __unicode__(self):
      return unicode(self.person) + ' ' + unicode(self.slot) + ' ' + self.LEVEL_DICT[self.level]
   class Meta:
      ordering = ('person',)

