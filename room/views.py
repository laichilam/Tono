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
    
    return render(request,'room/roomdetail.html',{
        'room':r
    })