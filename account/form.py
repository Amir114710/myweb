from django import forms
from django.urls import reverse
from matplotlib import widgets
from account.models import User
from django.core.validators import ValidationError
from django.contrib.auth import authenticate, login

class RegisterationForm(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':"نام کاربری" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))
    email = forms.EmailField(max_length=50 , widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder':"ایمیل" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':"گذرواژه" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':"تکرار گذرواژه" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))    


    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if password2 != password:
            raise ValidationError('this passwords are not same')
        # user = User.objects.create_user(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password') ,  email = self.cleaned_data.get('email'))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':"نام کاربری" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':"گذرواژه" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))    