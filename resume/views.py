from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from account.models import User
from .models import Skill , ResumePost

class ResumeView(TemplateView):
    template_name = 'resume/resume.html'

    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        context['skill'] = Skill.objects.all()
        context['resume'] = ResumePost.objects.all()
        return context
