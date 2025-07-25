from django.shortcuts import *
from books.forms import Create_book_form,Update_book_form,Payment_form
from author.models import Authors_profile
from books.models import All_books
from books.models import Rented_books
# Create your views here.
def create_books(request):
    if request.method=="POST":
        form=Create_book_form(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.author=Authors_profile.objects.get(author=request.user)
            book.save()
            return redirect('author_profile')
        else:
            print(form.errors)
    else:
        form=Create_book_form()
    return render(request,'create_book.html',{'form':form})


def read_books(request,id):
    if request.user.is_authenticated:
        books=get_object_or_404(All_books,pk=id)
        return render(request,'read_books.html',{'books':books})
    else:
        return redirect('student_reg')

def update_books(request,id):
    books=get_object_or_404(All_books,pk=id)
    if request.method=="POST":
        form=Update_book_form(request.POST,instance=books)
        if form.is_valid():
            form.save()
            return redirect('author_profile')
    else:
        form=Update_book_form(instance=books)
    return render(request,'update_books.html',{'form':form})


def all_books(request):
    books=All_books.objects.all()
    context={'books':books}
    print(books)
    return render(request,'total_books.html',context)

def delete_books(request,id):
    books=get_object_or_404(All_books,pk=id)
    if books:
        books.delete()
        return redirect('all_books')
    else:
        return render(request,'total_books.html')

    
def rent_book(request,id):
    print(id)
    book=get_object_or_404(All_books,pk=id)
    if not book.is_available:
        return HttpResponse("BOOK NOT AVAILABLE")
    
    if request.method=="POST":
        form=Payment_form(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            return_date=form.cleaned_data['return_date']
            # print(amount,return_date,"--------------------")
            book.is_available=False
            book.save()

            rent=Rented_books.objects.create(
                book=book,
                user=request.user,
                return_at=return_date,
                amount_paid=amount
            )
            return redirect('student_profile')
        else:
            print(form.errors)
        
    else:
        form=Payment_form()
    
    return render(request,'payment_page.html',{'form':form,'book':book})

