from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import room, roommessage
from .forms import roommessageform
# Create your views here.
#def new_room(request, code):
def new_room(request):
    c = "ABCDABCD"
    roommes = room.objects.filter(code='ABCDABCD').filter(members__in=[request.user.id])

    if roommes:
        pass
    if request.method == 'POST':
        form = roommessageform(request.POST)
        
        if form.is_valid():
            rm = room.objects.create(code=c)
            rm.members.add(request.user)
            rm.save()

            rmes = form.save(commit=False)
            rmes.room = rm
            rmes.created_by = request.user
            rmes.save()

            return redirect('index')
    else:
        form = roommessageform()
    return render(request, 'room/new.html',{
        'form': form
    })

@login_required
def all_room(request):
    rooms = room.objects.filter(members__in=[request.user.id]).order_by('modified_at')

    return render(request,'room/roomlist.html', {
        'rooms':rooms
    })