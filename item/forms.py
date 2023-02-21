from django import forms
from .models import Note

class newNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name','detail','priority','inlist',)