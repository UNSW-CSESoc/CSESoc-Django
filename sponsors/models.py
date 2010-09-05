from django.db import models
from django.template.loader import render_to_string
from datetime import date
from django.template import RequestContext
from csesoc import settings

class Sponsor(models.Model):
   name = models.CharField(max_length = 200)
   rank = models.IntegerField()
   description = models.TextField(blank = True)
   website = models.URLField(verify_exists = False)
   logo = models.ImageField(upload_to = 'sponsors')
   alt_text = models.CharField(max_length = 150)

   def __unicode__(self):
     return self.name

   def get_rendered_sidebar_html(self):
      return render_to_string("sponsor-sidebar.html", { 'object': self, 'MEDIA_URL' : settings.MEDIA_URL }) 

   def get_rendered_html(self):
     return render_to_string("sponsor-description.html", { 'object': self, 'MEDIA_URL' : settings.MEDIA_URL })
