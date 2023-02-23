from django import forms
from .models import room, roommessage

class roommessageform(forms.ModelForm):
    class Meta:
        model = roommessage
        labels = {'content':'',}
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'rows':2,
                'class':'text-2xl bg-alu-three rounded-xl border px-4 py-4',
                'placeholder':"Type your message here.",
            })
        }

class roomform(forms.ModelForm):
    class Meta:
        model = room
        fields = ('name','code',)

class joinform(forms.ModelForm):
    class Meta:
        model = room
        fields = ('code',)