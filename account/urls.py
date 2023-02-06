from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path("register", views.RegisterationView.as_view() , name="register"),
    path('login' , views.LoginView.as_view() , name="login"), 
    path('logout' , views.logout_user , name="logout"),
] 