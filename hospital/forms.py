# forms.py
from django import forms
from .models import hospital, department

class hospitalForm(forms.ModelForm):
    class Meta:
        model = hospital
        fields = ['hospital_name', 'department']

    # department = forms.ModelMultipleChoiceField(
    #     queryset=department.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
