from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Moc, Exhibition

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
        fields = ("author", "title", "category", "size", "poster",)

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ("date", "city", "address", "principal", "required_area", "comments",)




