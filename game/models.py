from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.template.loader import render_to_string
from datetime import datetime

class Static(models.Model):
   title = models.CharField(max_length=200)
   text = models.TextField()
   creation_date = models.DateTimeField(auto_now_add=True)
   update_date = models.DateTimeField(auto_now=True)
   slug = models.SlugField(help_text="slug will be used in url generation, keep it simple, stupid.")
   def __unicode__(self):
      return self.title

