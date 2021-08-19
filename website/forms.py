from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse


class ContactForm(forms.Form):
    name = forms.CharField(max_length=31)
    email = forms.EmailField()
    tel = forms.CharField(max_length=31)
    message = forms.CharField(max_length=1023)