from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import room, roommessage
from .forms import roommessageform, roomform
# Create your views here.
#def new_room(request, code):

@login_required
def new_room(request):
    form = roomform()
    if request.method == 'POST':
        form = roomform(request.POST)

        if form.is_valid():
            rm = form.save(commit=False)
            rm.created_by = request.user
            rm.save()
            rm.members.add(request.user)
            return redirect('roomlist')
    else:
        form = roomform()
    return render(request, 'room/newroom.html',{
            'form': form
        })

@login_required
def all_room(request):
    rooms = room.objects.filter(members__in=[request.user.id]).order_by('modified_at')

    return render(request,'room/roomlist.html', {
        'rooms':rooms
    })

def roomdetail(request, pk):
    r = get_object_or_404(room, members__in = [request.user.id], pk=pk)
    messages = roommessage.objects.filter(room = r).order_by('created_at')

    if request.method =='POST':
        form = roommessageform(request.POST)
        if form.is_valid():
            mes = form.save(commit=False)
            mes.room = r
            mes.created_by = request.user
            mes.save()
            return redirect('roomdetail', pk=pk)
    else:    
        form = roommessageform()

    return render(request,'room/roomdetail.html',{
        'room' : r,
        'form' : form,
        'room_messages' : messages,
    })

def newmes(request, pk):
    if request.method =='POST':
        form = roommessageform(request.POST)
        if form.is_valid():
            mes = form.save(commit=False)
            mes.room = room.objects.filter(pk=pk)
            mes.created_by = request.user
            mes.save()
            return redirect('.')
    else:    
        form = roommessageform()

    return render(request,'room/roomdetail.html',{
        'form': form,
        'rid': pk,
    })