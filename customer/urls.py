from django.urls import path
from customer.views import *
urlpatterns = [
    path('',student_reg,name='student_reg'),
    # path('student_login/',student_login,name='student_login'),
    path('student_profile/',student_profile,name='student_profile'),
    path('student_logout/',student_logout,name='student_logout'),
    path('student_profile_update/',student_profile_update,name='student_profile_update'),
]
