from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from account.models import User
from .models import Work , Categories

class WorkView(ListView):
    model = Work
    template_name = "works/works_v2.html"
    context_object_name = 'works'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        context['categories'] = Categories.objects.all()
        return context
