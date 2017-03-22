from django import forms

class loginform(forms.Form):
    username = forms.CharField(max_length=10, min_length=3, label='username')
    password = forms.PasswordInput()


