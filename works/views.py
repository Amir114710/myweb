from django.shortcuts import render
from django.views.generic import TemplateView
from account.models import User


class WorkView(TemplateView):
    template_name = "works/works_v2.html"
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        return context
