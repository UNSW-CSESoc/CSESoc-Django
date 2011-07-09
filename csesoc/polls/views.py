from polls.models import Poll, PollOption
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

def castvote(request, id, error = None):
    poll = get_object_or_404(Poll, pk = id)
    return render_to_response('polls/vote.html', 
                                {'poll': poll, 'error': error}, 
                                context_instance = RequestContext(request))

def processvote(request, id):
    poll = get_object_or_404(Poll, pk = id)
    
    try:
        option = poll.polloption_set.get(pk = request.POST['option'])
    except (KeyError, PollOption.DoesNotExist):
        return redirect(reverse('polls.views.castvote', args = (poll.id, "error")))
    else:
        option.votes += 1
        option.save()
        return redirect(reverse('polls.views.results', args = (poll.id,)))

def results(request, id):
    poll = get_object_or_404(Poll, pk = id)
    return render_to_response('polls/results.html', 
                                {'poll': poll}, context_instance = RequestContext(request))
