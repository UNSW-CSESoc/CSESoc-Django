from django.db import models
from django import forms

# Create your models here.
class SuggestionForm(forms.Form):
  subject = forms.CharField(max_length=100)
  message = forms.CharField(widget=forms.Textarea(), initial="Replace with your suggestion.")
  sender = forms.EmailField(required=False)
