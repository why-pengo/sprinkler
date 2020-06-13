from django import forms


class SchedulerForm(forms.Form):
    dow = forms.CharField(max_length=7)
    start = forms.TimeField()
    end = forms.TimeField()
    zone = forms.IntegerField()
    active = forms.BooleanField()
    run_once = forms.BooleanField()
