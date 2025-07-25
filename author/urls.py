from django.urls import path
from author.views import *
urlpatterns = [
    path('',author_reg,name="author_reg"),
    path('author_profile/',author_profile,name="author_profile"),
    # path('author_login/',author_login,name="author_login"),
    path('author_logout/',author_logout,name="author_logout"),
    path('author_profile_update/',author_profile_update,name="author_profile_update"),
    path('all_author/',all_author,name="all_author"),
    
]

