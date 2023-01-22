from django.shortcuts import render
from django.views.generic import TemplateView
from account.models import User


class TestView(TemplateView):
    template_name = "home_app/index.html"

