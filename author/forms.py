from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from author.models import Authors_profile

class Author_reg_form(UserCreationForm):

    password1=forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'})
        )
    
    password2=forms.CharField(
        label=('Confirm Password'),
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'})
        )
    
    class Meta:
        model=User
        fields=['username','first_name','email']
        labels={'username':'Username','first_name':'Full Name','email':'Email ID'}
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Username','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'first_name':forms.TextInput(attrs={'placeholder':'Full Name','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'email':forms.TextInput(attrs={'placeholder':'Email ID','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),
        }


class Author_login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))


class Author_update_form(forms.ModelForm):
    class Meta:
        model=Authors_profile
        fields='__all__'
        exclude=('author',)
        widgets={
            'author_img':forms.FileInput(attrs={'placeholder':'Username','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'author_name':forms.TextInput(attrs={'placeholder':'Full Name','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'author_education':forms.TextInput(attrs={'placeholder':'Qualifications','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'author_books':forms.TextInput(attrs={'placeholder':'Books by You','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'author_mob':forms.TextInput(attrs={'placeholder':'Mobile','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'author_email':forms.TextInput(attrs={'placeholder':'Email ID','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'author_about':forms.TextInput(attrs={'placeholder':'About YourSelf','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),
        }
        

