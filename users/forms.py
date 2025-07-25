from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField


class User_login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))