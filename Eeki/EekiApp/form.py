from django import forms
from .models import ChangeStatus
 

class Form(forms.ModelForm):
    
    class Meta:
        model = ChangeStatus
        fields = "__all__"