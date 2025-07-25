from django import forms
from books.models import All_books

class Create_book_form(forms.ModelForm):
    class Meta:
        model=All_books
        fields='__all__'
        exclude=('author',)
        labels={'book_id':'Book No','book_title':'Book Name','book_content':'Book Content'}

        widgets={
            'book_id':forms.TextInput(attrs={'placeholder':'Book No','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mt-1'}),

            'book_title':forms.TextInput(attrs={'placeholder':'Book Name','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mt-1'}),

            'book_content':forms.Textarea(attrs={'placeholder':'Book Content','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mt-1'}),
        }

    

class Update_book_form(forms.ModelForm):
    class Meta:
        model=All_books
        fields='__all__'
        exclude=('author',)

        labels={'book_id':'Book No','book_title':'Book Name','book_content':'Book Content'}

        widgets={
            'book_id':forms.TextInput(attrs={'placeholder':'Book No','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mt-1'}),

            'book_title':forms.TextInput(attrs={'placeholder':'Book Name','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mt-1'}),

            'book_content':forms.Textarea(attrs={'placeholder':'Book Content','class':'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mt-1'}),
        }


class Payment_form(forms.Form):
    amount=forms.DecimalField()
    return_date=forms.DateField()
