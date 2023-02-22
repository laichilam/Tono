from django import forms
from .models import room, roommessage

class roommessageform(forms.ModelForm):
    class Meta:
        model = roommessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class':'w-full py-4 px-8 rounded-xl border'
            })
        }

class roomform(forms.ModelForm):
    class Meta:
        model = room
        fields = ('name','code',)
