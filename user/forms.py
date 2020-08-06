from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(label='اسم المستخدم')
    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'email' , 'password')