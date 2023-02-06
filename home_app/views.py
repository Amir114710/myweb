from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About , Activity
from account.models import User , Profile

class TestView(TemplateView):
    template_name = "home_app/index.html"

    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['about'] = About.objects.all()
        context['activity'] = Activity.objects.all()
        context['user'] = Profile.objects.all()
        return context

