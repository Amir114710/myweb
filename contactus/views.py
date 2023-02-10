from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView , FormView
from account.models import Profile
from .form import ContactUs
from .models import Contact
from django.contrib.auth import authenticate, login


class ContactView(FormView):
    template_name = "contactus/contact.html"
    form_class = ContactUs
    success_url = reverse_lazy('home:main')
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        return context
    def form_valid(self, form):
        cd = form.cleaned_data
        Contact.objects.create(username = cd['username'] , email = cd['email'] , message = cd['message'])
        return redirect(reverse_lazy('contact:success'))
    
class ThanksPageView(TemplateView):
    template_name = 'contactus/Thanks_page.html'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        return context
