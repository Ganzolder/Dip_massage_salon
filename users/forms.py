from django.contrib.auth.forms import UserCreationForm

from service.forms import StyleFormMixin
from users.models import User, Masseur
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class MasseurForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Masseur
        fields = ('name', 'surname', 'phone', 'description', 'photo')
