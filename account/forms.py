from typing import Any
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 30,label="Username")
    password = forms.CharField(max_length = 10,label="Password",widget=forms.PasswordInput)
    confirm= forms.CharField(max_length = 10,label="Confirm pasword",widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data["username"]
        password=self.cleaned_data["password"]
        confirm=self.cleaned_data["confirm"]

        if username and password and password != confirm:
            raise forms.ValidationError("sifreler duz deil")
        values={
            "username":username,
            "password":password
        }

        return values
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30,label="Username")
    password = forms.CharField(max_length = 10,label="Password",widget=forms.PasswordInput)
   

    