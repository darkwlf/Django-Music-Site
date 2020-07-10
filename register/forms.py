from django import forms

class UserForm(forms.Form):

    username= forms.CharField(max_length=100)

    email= forms.EmailField()

    number = forms.IntegerField()

    name = forms.CharField(max_length=100)

    password = forms.CharField(max_length=400)

class LoginForm(forms.Form):

    username= forms.CharField(max_length=100)

    password = forms.CharField(max_length=400)



