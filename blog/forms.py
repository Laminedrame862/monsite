from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
           model = Message
           fields = ['nom', 'email', 'texte']
           widgets = {
               'nom': forms.TextInput(attrs={'class': 'form-control'}),
               'email': forms.EmailInput(attrs={'class': 'form-control'}),
               'texte': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
           }