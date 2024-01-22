from django import forms
from django.forms import ModelForm
from .models import Event, Venue


class EventForm(ModelForm):
    time = forms.TimeField(
        # input_formats=['%I:%M %p'],
        # widget=forms.TimeInput(format='%H:%M:%p')
    )

    class Meta:
        model = Event
        fields = ['name', 'venue', 'description', 'date', 'time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['venue'].queryset = Venue.objects.all()

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location', 'description']

