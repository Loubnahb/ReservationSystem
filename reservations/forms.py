# forms.py
from django import forms
from .models import Reservation
from django.contrib.auth import get_user_model

User = get_user_model()

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['title', 'date', 'start_time', 'end_time', 'description', 'attendees']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            # salle is pre-filled, no need for it to be in the form
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Exclude the current user from the attendees queryset
        if user:
            self.fields['attendees'].queryset = User.objects.exclude(pk=user.pk)
