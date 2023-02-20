from django.shortcuts import render
from item.models import Note, NoteList, Process
import requests
# Create your views here.

def index(request):
    response=requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
    json_response = response.json()
    joke = json_response['joke']
    sum = Note.objects.all().count()
    finished = Note.objects.filter(complete=True).count()
    unfinished = sum - finished
    return render(request,'core/index.html', {
        'sum': sum,
        'fin': finished,
        'unfin': unfinished,
        'r':joke,
    })

def base(request):
    return render(request,'core/base.html',{})

def notes(request):
    notes = Note.objects.all().order_by('-priority')
    sum = notes.count()
    finished = Note.objects.filter(complete=True).count()
    unfinished = sum - finished
    return render(request,'core/notes.html', {
        'notes': notes,
        'sum': sum,
        'fin': finished,
        'unfin': unfinished,
    })