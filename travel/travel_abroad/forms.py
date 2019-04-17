from django import forms
from django.contrib.auth.models import User
from travel_abroad.models import UserprofileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User

        fields = ('first_name', 'last_name', 'email', 'password')

class UserprofileInfoForm(forms.ModelForm):

    class Meta():
        model = UserprofileInfo
        fields = ('profile_pic',)
