from csesoc.polls.models import Poll, PollOption, Vote
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime

@login_required
def castvote(request, id, error = None):
    poll = get_object_or_404(Poll, pk = id)

    return render_to_response('polls/vote.html', 
                                {'poll': poll, 'error': error}, 
                                context_instance = RequestContext(request))

@login_required
def processvote(request, id):
    poll = get_object_or_404(Poll, pk = id)

    #Poll has ended
    if (poll.endDate < datetime.now()):
        return render_to_response('polls/results.html',
                                    {'poll': poll, 'error': "This poll has already ended."},
                                    context_instance = RequestContext(request))
    #Check if user has alredy voted
    elif (Vote.objects.filter(username = request.user.username).filter(poll = poll).count() == 0):
        try:
            option = poll.polloption_set.get(pk = request.POST['option'])
        #No option selected
        except (KeyError, PollOption.DoesNotExist):
            return render_to_response('polls/vote.html',
                                        {'poll': poll, 'error': "You must select an option."},
                                        context_instance = RequestContext(request))
        #Successful vote
        else:
            option.votes += 1
            option.save()
            Vote(username = request.user.username, poll = poll).save()

            return redirect(reverse('polls.views.results', args = (id,)))
    else:
        return render_to_response('polls/results.html',
                                    {'poll': poll, 'error': "You have already voted on this poll. Your vote has not been counted."},
                                    context_instance = RequestContext(request))

def results(request, id, error = None):
    poll = get_object_or_404(Poll, pk = id)
    return render_to_response('polls/results.html', 
                                {'poll': poll, 'error': error}, 
                                context_instance = RequestContext(request))

def index(request):
    return render_to_response('polls/index.html',
                                {'openPolls': Poll.objects.all().filter(pubDate__gt=datetime.now()).order_by("-pubDate"),
                                'closedPolls': Poll.objects.all().filter(pubDate__lte=datetime.now()).order_by("-pubDate")},
                                context_instance = RequestContext(request))
                                
