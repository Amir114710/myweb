from django.shortcuts import render
from django.shortcuts import render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView
from mixins import LoginRequirdMixins , LogoutRequirdMixins
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
from .form import LoginForm, RegisterationForm
from .models import User , Profile

class LoginView(LoginRequirdMixins , FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:main')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = Profile.objects.all()
        return context
    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request , username=cd['username'] , password=cd['password'])
        if user is not None:
            login(self.request , user)
            return redirect(reverse_lazy('home:main'))
        else:
            return redirect(reverse_lazy('account:login'))

class RegisterationView(LoginRequirdMixins , FormView):
    template_name = 'account/registeration.html'
    form_class = RegisterationForm
    success_url = reverse_lazy('home:main')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = Profile.objects.all()
        return context
    def form_valid(self, form):
        if self.request.user.is_authenticated == True:
            return redirect(reverse('home:main'))
        else:
            cd = form.cleaned_data
            user = User.objects.create_user(username = cd['username'] , password = cd['password'])
            login(self.request , user)
            return redirect(reverse_lazy('home:main'))

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home:main')
    else:
        return redirect('home:main')



