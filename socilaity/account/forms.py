from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email", )

    def clean_password2(self):
        cleaned_data = self.cleaned_data

        if cleaned_data["password"] != cleaned_data["password2"]:
            raise forms.ValidationError("Passwords don't match!")

        return cleaned_data["password2"]
