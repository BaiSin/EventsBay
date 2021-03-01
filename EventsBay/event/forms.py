from django import forms
from .models import eventlist

class EventForm(forms.ModelForm):
    class Meta:
        model = eventlist
        fields = ['event_name', 'data', 'date', 'location', 'image',]