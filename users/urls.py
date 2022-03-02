from django.urls import path
from .views import UserLoginView, UserRegisterPage
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'users:login'), name='logout'),
    path('register/', UserRegisterPage.as_view(), name='register'),
    
]