from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .forms import newNoteForm
from .models import Note

# Create your views here.
def newnote(request):
    if request.method =='POST':
        form = newNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            return redirect('notes')
    else:    
        form = newNoteForm()

    return render(request,'item/newnote.html',{
        'form': form
    })

def notedetail(request, pk):
    note = get_object_or_404(Note, created_by = request.user, pk=pk)
    
    return render(request,'item/notedetail.html',{
        'note':note
    })

def deletenote(request, pk):
    note = get_object_or_404(Note, created_by = request.user, pk=pk)
    note.delete()

    messages.success(request, 'Note Deleted.')
    return redirect('notes')