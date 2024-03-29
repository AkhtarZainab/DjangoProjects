from django import forms

class RegForm(forms.Form):
    FirstName = forms.CharField(max_length=10)
    LastName = forms.CharField(max_length=10)
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    Cpassword = forms.CharField(max_length=10, widget=forms.PasswordInput())
    MobileNumber = forms.IntegerField()
    EmailId = forms.EmailField()


class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())