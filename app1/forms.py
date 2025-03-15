from django import forms
from .models import Patient

class Patientforms(forms.ModelForm):
    class Meta:
        model = Patient
        fields =['name'
                 ,'age',
                 'gender',
                 'contact',
                 'address',
                 'date',
                 'disease_diagnosed',
                 'case_details',
                 'medications'
                 
                 ]


