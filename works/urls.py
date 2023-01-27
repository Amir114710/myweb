from django.urls import path
from . import views

app_name = "work"

urlpatterns = [
    path('' , views.WorkView.as_view() , name='main_work')
]