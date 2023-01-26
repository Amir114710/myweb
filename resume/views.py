from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from account.models import User
from .models import Skill , ResumePost

class ResumeView(ListView):
    model = ResumePost
    template_name = 'resume/resume.html'
    context_object_name = 'resume'

    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        context['skill'] = Skill.objects.all()
        return context

class DetailResume(DetailView):
    model = ResumePost
    template_name = 'resume/single-post.html'
    context_object_name = 'resumes'

    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        return context