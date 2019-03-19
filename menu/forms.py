from django import forms
from django.forms import ModelForm, Textarea
from .models import pppoe_login, url

class pppoe_config_form(forms.ModelForm):
    class Meta:
        model = pppoe_login
        fields = ('username', 'password')

class UrlAdditionForm(forms.ModelForm):
    class Meta:
        model = url
        fields = ('url_name',)