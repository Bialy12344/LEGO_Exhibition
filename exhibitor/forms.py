from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ("nick", "password", "name", "surname","phone_number","email_adress",)
