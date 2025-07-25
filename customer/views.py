from django.shortcuts import *
from customer.forms import Student_reg_form,Student_login_form,Student_update_form
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from customer.models import students_profile
from books.models import Rented_books
# Create your views here.
def student_reg(request):
    if request.method == 'POST':
        form = Student_reg_form(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='student')  # Unpack the tuple
            user.groups.add(group)  # Add the Group object
            return redirect("user_login")
        else:
            print(form.errors)
    else:
        form = Student_reg_form()
    return render(request, 'student_reg.html', {'form': form})


# def student_login(request):
#     if request.method=="POST":
#         form=Student_login_form(request=request,data=request.POST)
#         if form.is_valid():
#             user=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user_type=request.POST.get('user_type')
#             print(user_type)
#             user=authenticate(username=user,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('student_profile')
#             else:
#                 print("User not found")
#         else:
#             print(form.errors)
#     form=Student_login_form()
#     return render(request,'students_login.html',{'form':form})   


def student_profile(request):
    if request.user.is_authenticated:
        student_pro=get_object_or_404(students_profile,student=request.user)
        # rented_books=get_object_or_404(Rented_books,user=request.user)
        # print(rented_books)
        context={'student_pro':student_pro}
        return render(request,'student_profile.html',context)
    else:
        return redirect('student_login')

def student_logout(request):
    logout(request)
    return redirect('all_books')


def student_profile_update(request):
    if request.user.is_authenticated:
        student_pro=get_object_or_404(students_profile,student=request.user)
        if request.method=="POST":
            form=Student_update_form(request.POST,request.FILES,instance=student_pro)
            if form.is_valid():
                form.save()
                return redirect('student_profile')
            else:
                print(form.errors)
                return HttpResponse("Something went wrong")

        else:
            form=Student_update_form(instance=student_pro)
        return render(request,'student_profile_update.html',{'form':form})