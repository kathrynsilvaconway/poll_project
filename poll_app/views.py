from django.shortcuts import render, redirect

from .forms import NewPollForm
from .models import Poll

def index(request):
    context = {
        'polls': Poll.objects.all()
    }
    return render(request, 'index.html', context)

def make_poll(request):
    if request.method == 'POST':
        form = NewPollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewPollForm()
        context = {
            'form': form
        }
        return render(request, 'make_poll.html', context)
    return render(request, 'make_poll.html')

def vote(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        selection = request.POST['poll']
        if selection == 'one':
            poll.one_count += 1
        if selection == 'two':
            poll.two_count += 1
        if selection == 'three':
            poll.three_count += 1
        poll.save()
        return redirect(f'/display_results/{poll_id}')
    context = {
        'poll':poll
    }
    return render(request, 'vote.html', context)

def display_results(request, poll_id):
    context = {
        'poll': Poll.objects.get(id=poll_id)
    }
    return render(request, 'display_results.html', context)

def delete_poll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('/')
    context = {
        'poll': poll
    }
    return render(request, 'delete_poll.html', context)


# Create your views here.
