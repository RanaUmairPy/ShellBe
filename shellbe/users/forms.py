
from django import forms
from .models import CUser 

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
     

    class Meta:
        model = CUser  
        fields = ['first_name', 'last_name', 'username','email', 'phone_number', 'user_profile', 'password']

    def save(self, commit=True):
        user = super().save(commit=False) 
        user.set_password(self.cleaned_data['password'])  
        if commit:
            user.save() 
        return user
