from django import forms

from .models import Tickets

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model=Tickets
        fields=['title','summary',]
        widgets={
             'title' : forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}),
            'summary' : forms.Textarea(attrs={'placeholder':'Summary','class':'form-control'}),
        }