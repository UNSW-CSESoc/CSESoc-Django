from django.db import models

class Suggestion(models.Model):
   subject = models.TextField(max_length=100)
   message = models.TextField()
   sender = models.EmailField()
   created = models.DateTimeField()
   last_modified = models.DateTimeField()

   def __unicode__(self):
      return "Suggestion: %s" % self.subject

class Comment(models.Model):
   suggestion = models.ForeignKey(Suggestion)
   name = models.CharField(max_length=50)
   comment = models.TextField()
   created = models.DateTimeField()

   def __unicode__(self):
      return unicode(self.name) + ": " + unicode(self.comment[0:50] + "...")
