from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True, min_length=10, max_length=250)
