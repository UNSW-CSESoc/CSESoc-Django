from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pubDate = models.DateTimeField('Date published')

    def __unicode__(self):
        return self.question

class PollOption(models.Model):
    poll = models.ForeignKey(Poll)
    description = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.description
