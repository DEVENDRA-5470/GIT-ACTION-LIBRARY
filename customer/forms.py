from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm
from customer.models import students_profile



class Student_reg_form(UserCreationForm):

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

class Student_login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))




class Student_update_form(forms.ModelForm):
    class Meta:
        model=students_profile
        fields='__all__'
        exclude=('student','student_rented_books')
        widgets={
            'student_img':forms.FileInput(attrs={'placeholder':'Username','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'student_name':forms.TextInput(attrs={'placeholder':'Full Name','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'student_education':forms.TextInput(attrs={'placeholder':'Qualifications','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            # 'student_rented_books':forms.TextInput(attrs={'placeholder':'Books by You','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'student_mob':forms.TextInput(attrs={'placeholder':'Mobile','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'student_email':forms.TextInput(attrs={'placeholder':'Email ID','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),

            'student_about':forms.TextInput(attrs={'placeholder':'About YourSelf','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),
        }
        

