from django.urls import path
from users.views import user_profile_redirect,user_login

urlpatterns = [
    path('profile/',user_profile_redirect,name="profile"),
    path('user_login/',user_login,name="user_login")
]
