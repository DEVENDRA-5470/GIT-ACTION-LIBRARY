from django.shortcuts import *
from customer.models import students_profile
from author.models import Authors_profile
from django.contrib.auth.models import Group
from users.forms import User_login_form
from django.contrib.auth import *
# Create your views here.

def user_profile_redirect(request):
    user=request.user
    
    if user.groups.filter(name="author").exists():
        if Authors_profile.objects.filter(author=user).exists():
            return redirect('author_profile')
        
    elif user.groups.filter(name="student").exists():
        if students_profile.objects.filter(student=user).exists():
            return redirect('student_profile')
    
    return HttpResponse("Something went wrong")



def user_login(request):
    if request.method=="POST":
        form=User_login_form(request=request,data=request.POST)
        if form.is_valid():
            user=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user_type=request.POST.get('user_type')
            print(user_type)
            user=authenticate(username=user,password=password)
            if user is not None:
                if user.groups.filter(name=user_type):
                    login(request,user)
                    return redirect('profile')
                else:
                    print(form.errors)
            else:
                print("User not found")
        else:
            print(form.errors)
    form=User_login_form()
    return render(request,'users_login.html',{'form':form})   
