
"""from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User"""
from users.models import Usercreate
from django import forms

"""class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password','password2']"""
        
class UserCreateform1(forms.ModelForm):
    class Meta:
        model = Usercreate
        fields = "__all__"