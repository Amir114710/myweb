from django.urls import path
from . import views

app_name = "work"

urlpatterns = [
    path('' , views.WorkView.as_view() , name='main_work'),
    path('detail/<slug:slug>' , views.WorkDetailView.as_view() , name="work_detail"),
    path('category/<int:pk>', views.Category_details.as_view() , name='category_detail'),
]