from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('' , views.ResumeView.as_view() , name="resume"), 
    path('detail/<slug:slug>' , views.DetailResume.as_view() , name="resume-detail")
]