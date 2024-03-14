from django import forms
from consultbotui.models import Schedules
from bootstrap_datepicker_plus import DateTimePickerInput


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = ['start_dt', 'end_dt', 'note', 'markup']
        widgets = {
            'start_dt': DateTimePickerInput(),
            'end_dt': DateTimePickerInput(),
        }
