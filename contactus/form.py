from django import forms
from django.urls import reverse
from matplotlib import widgets
from account.models import User
from django.core.validators import ValidationError
from django.contrib.auth import authenticate, login

class ContactUs(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':"نام کاربری" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))
    email = forms.EmailField(max_length=50 , widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder':"ایمیل" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"})) 
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"textarea form-control" , 'id':"messageContact" , 'name':"messageContact" , 'placeholder':"پیام..." , 'rows':"4" , 'required':"required" , 'oninvalid':"setCustomValidity('فیلد را پر کنید')" , 'onkeyup':"setCustomValidity('')"}))    