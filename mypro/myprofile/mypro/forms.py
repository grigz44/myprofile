from django import forms
from .models import *

class enquiryForm(forms.ModelForm):
    class Meta:
        model = enquiry
        fields = ('name','email','phone','message')
        widgets = {
            'name'     : forms.TextInput(attrs={'class':'form-control','id':'name','placeholder': 'Your Name'}),
            'email'    : forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder': 'Your Email'}),
            'phone'    : forms.TextInput(attrs={'pattern':'[1-9]{1}[0-9]{9}','class':'form-control','id':'phone','placeholder': 'Your Phone'}),
            'message'  : forms.Textarea(attrs={'style': 'height: 10em;','class':'form-control','id':'message','placeholder': 'message'}),
        }
        labels = {
        "name":  "",
        "email": "",
        "phone": "",
        "message":"",
        }