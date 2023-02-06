from django.shortcuts import render
from django.views.generic import TemplateView
from account.models import Profile


class BlogView(TemplateView):
    template_name = "blog/weblog.html"

    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        return context