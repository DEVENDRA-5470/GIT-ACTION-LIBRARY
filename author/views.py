from django.shortcuts import *
from author.forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from author.models import Authors_profile
from books.models import All_books
# Create your views here.
def author_reg(request):
    if request.method == 'POST':
        form = Author_reg_form(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='author')
            user.groups.add(group)
            return redirect("user_login")
        else:
            print(form.errors)
    else:
        form = Author_reg_form()
    return render(request, 'author_reg.html', {'form': form})



def author_profile(request):
    if request.user.is_authenticated:
        author_pro=get_object_or_404(Authors_profile,author=request.user)
        books=All_books.objects.filter(author=author_pro)
        
        context={'author_pro':author_pro,'books':books}
        return render(request,'author_profile.html',context)
    else:
        return redirect('users')


# def author_login(request):
#     if request.method=="POST":
#         form=Author_login_form(request=request,data=request.POST)
#         if form.is_valid():
#             user=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user=authenticate(username=user,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('author_profile')
#             else:
#                 print("User not found")
#         else:
#             print(form.errors)
#     form=Author_login_form()
#     return render(request,'author_login.html',{'form':form})

def author_logout(request):
    logout(request)
    return redirect('all_books')

def author_profile_update(request):
    if request.user.is_authenticated:
        author_pro=get_object_or_404(Authors_profile,author=request.user)
        if request.method=="POST":
            form=Author_update_form(request.POST,request.FILES,instance=author_pro)
            if form.is_valid():
                form.save()
                return redirect('author_profile')
            else:
                print(form.errors)
                return HttpResponse("Something went wrong")

        else:
            form=Author_update_form(instance=author_pro)
        return render(request,'author_profile_update.html',{'form':form})
    

def all_author(request):
    data=Authors_profile.objects.all()
    return render(request,'all_author.html',{'data':data,})


