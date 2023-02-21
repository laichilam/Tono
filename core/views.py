from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Note, NoteList, Process
import requests
# Create your views here.

#@login_required
def index(request):
    r = getJoke()
    if request.user.is_authenticated:
        us = request.user

        sum = Note.objects.filter(created_by = us).count()
        finished = Note.objects.filter(created_by = us, complete=True).count()
        unfinished = sum - finished
    
        return render(request,'core/index.html', {
            'sum': sum,
            'fin': finished,
            'unfin': unfinished,
            'r':r,
        })
    else:
        return render(request,'core/index.html', {
            'sum': -1,
            'fin': -1,
            'unfin': -1,
            'r':r,
        })

def getJoke():
    response=requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
    json_response = response.json()
    joke = json_response['joke']
    return joke

def base(request):
    return render(request,'core/base.html',{})

@login_required
def notes(request):
    notes = Note.objects.filter(created_by = request.user).order_by('-priority')
    sum = notes.count()
    finished = Note.objects.filter(created_by = request.user, complete=True).count()
    unfinished = sum - finished
    return render(request,'core/notes.html', {
        'notes': notes,
        'sum': sum,
        'fin': finished,
        'unfin': unfinished,
    })