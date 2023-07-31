from django import forms
from django.forms import TextInput
from .models import *

class num_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(num_status, self).__init__(*args, **kargs)
    class Meta:
        model = number
        fields = ['phone_number']
        widgets = {
            'phone_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter your phone number'
                })
        }

class otp_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(otp_status, self).__init__(*args, **kargs)
    class Meta:
        model = otp_verify
        fields = ['otp']
        widgets = {
            'otp': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter the OTP'
                })
        }
        
class final_otp_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(final_otp_status, self).__init__(*args, **kargs)
    class Meta:
        model = final_otp
        fields = ['f_otp']
        widgets = {
            'f_otp': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter the OTP'
                })
        }
        
class qr_code_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(qr_code_status, self).__init__(*args, **kargs)
    class Meta:
        model = qr_code
        fields = ['qr_code_value']
        widgets = {
            'qr_code_value': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter the OTP'
                })
        }
class upload_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(upload_status, self).__init__(*args, **kargs)
    class Meta:
        model = upload
        fields = ['upload_file']