from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from account.models import Profile
from .models import Post


class BlogView(ListView):
    model = Post
    template_name = "blog/weblog.html"
    context_object_name = 'posts'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        return context
    
class PostDetail(DetailView):
    model = Post
    template_name = "blog/detailpage.html"
    context_object_name = 'posts'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        return context 
