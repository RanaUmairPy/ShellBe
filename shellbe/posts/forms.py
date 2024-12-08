from django import forms
from posts.models import Posts


class Postform(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'