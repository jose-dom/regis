from django import forms
from .models import Visitor
from django.core import validators


class NewUserForm(forms.ModelForm):
    class Meta():
        model = Visitor
        fields = ('first_name', 'last_name', 'email', 'purpose1', 'purpose2', 'purpose3', 'purpose4', 'purpose5', 'purpose6', 'purpose7', 'purpose8')


class FirstTimeUserForm(forms.ModelForm):
    class Meta():
        model = Visitor
        fields = ('address', 'referral', 'gender')