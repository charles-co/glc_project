from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateTimeRangeField, RangeWidget

class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'photo', 'location', 'start', 'end', 'description']

    def clean(self):
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        if start is not None and end is not None:
            if start > end:
                raise forms.ValidationError("Dates are incorrect.")
        return self.cleaned_data