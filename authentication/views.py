from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm


class LoginView(View):
    template_name = 'authentication/login.html'

    def get(self, request):

        return render(request, self.template_name)


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user  = authenticate(
            email = email, 
            password =  password
        )
        if user is not None:
            login(request, user)
            if  user.is_customer:
                return redirect('home')
            if user.is_staff:
                return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')


class SignUpView(View):

    template_name =  'authentication/signup.html'
    form_class = UserRegistrationForm

    def get(self, request):
        form  =  self.form_class
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign Up Successfully!!')
            return redirect('login')
        else:
            return render(request, self.template_name, context={
                'form': form
            })
        


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')