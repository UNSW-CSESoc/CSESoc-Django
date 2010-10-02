# Create your views here.
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from models import Suggestion, Comment
from csesoc import settings
from django.template import RequestContext
from django.http import Http404
from django import forms
from datetime import datetime

def comments(request, suggestion):
   this_suggestion = Suggestion.objects.get(id=suggestion)

   comment_form = CommentForm()
   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
         clean_name = form.cleaned_data['name']
         clean_comment = form.cleaned_data['comment']

         # create and save the new comment
         stamp = datetime.now()
         new_comment = Comment(
                        suggestion=this_suggestion, 
                        name=clean_name, 
                        comment=clean_comment,
                        created = stamp
                        )
         new_comment.save()

         # update the timestamp of the parent
         this_suggestion.last_modified = stamp
         this_suggestion.save()

      else:
         comment_form = form

   comments_for_suggestion = Comment.objects.filter(suggestion=suggestion)
   return render_to_response('suggestion_with_comments.html', 
               RequestContext(request, {
                  'comments': comments_for_suggestion,
                  'suggestion': this_suggestion,
                  'form': comment_form
               }))

class CommentForm(forms.Form):
   name = forms.CharField(min_length=1, max_length=50)
   comment = forms.CharField(widget=forms.Textarea())

def suggest(request):
  if request.method == 'POST':
    form = SuggestionForm(request.POST)
    if form.is_valid():
      clean_subject = form.cleaned_data['subject']
      clean_message = form.cleaned_data['message']
      clean_sender = form.cleaned_data.get('sender', 'anon@csesoc.cse.unsw.edu.au')

      stamp = datetime.now()
      suggestion = Suggestion(
                        subject = clean_subject, 
                        message = clean_message, 
                        sender = clean_sender,
                        created = stamp,
                        last_modified = stamp
                        )
      suggestion.save()

      # send an email to the suggestions mailing list
      #send_mail('Suggestion: %s' % clean_subject, clean_message, clean_sender, ['csesoc.suggestions@cse.unsw.edu.au'])
      #send_mail('Suggestion: %s' % subject, message, sender, ['csesoc.sysadmin.head@cse.unsw.edu.au'])

      return render_to_response('thanks-suggestion.html', context_instance=RequestContext(request))
  else:
    form = SuggestionForm()

  return render_to_response('suggest.html', context_instance=RequestContext(request, {'form': form}))

class SuggestionForm(forms.Form):
   subject = forms.CharField(max_length=100)
   message = forms.CharField(widget=forms.Textarea(), initial="Replace with your suggestion.")
   sender = forms.EmailField(required=False)

def list_suggestions(request):
   suggestions = Suggestion.objects.order_by('-last_modified')
   return render_to_response('list_suggestions.html', 
         context_instance=RequestContext(request, {'suggestions': suggestions}))

