from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Moc

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ("username", "name", "surname", "phone_number", "email_adress",)
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "name", "surname", "phone_number", "email_adress",)

class MocForm(forms.ModelForm):
    class Meta:
        model = Moc
        fields = ("author", "title", "poster",)


