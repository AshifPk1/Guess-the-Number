from django import forms

class UserForm(forms.Form):
    number= forms.IntegerField(label='Enter your guess')

