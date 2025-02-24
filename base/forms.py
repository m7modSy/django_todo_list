from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django import forms
from todo_list.utils.widgets import CustomRadioSelect
from django.forms import RadioSelect

class UserForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model=User
        fields = ['username', 'password1', 'password2']