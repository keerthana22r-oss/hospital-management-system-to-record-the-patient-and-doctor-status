from django import forms
from .models import Hospital

class HospitalForm(forms.ModelForm): #form
    class Meta: # to replace the input tag
        model=Hospital
        fields=['name','disease','doctor_assigned','age','room_number']