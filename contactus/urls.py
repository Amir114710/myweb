from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('' , views.ContactView.as_view() , name='main_contact'),
    path('success' , views.ThanksPageView.as_view() , name='success')
]

