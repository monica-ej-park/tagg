from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login, logout, authenticate
from .models import User
from django.views import View
from .forms import SignupForm, LoginForm


class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/forum/list/')
        
        context = {
            'form': SignupForm()
        }
        return render(request, 'account/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(email=email, password=raw_password)
            login(request, user)
            # 게시글 목록 페이지
            return redirect('/forum/list/')

        context = {
            'form': form
        }
        return render(request, 'account/signup.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html', {'form': LoginForm()} )

    def post(self, request):
        form = LoginForm(request.POST)
        email = request.POST['email']
        pw = request.POST['password']
        user = authenticate(email=email, password=pw)
        if user: 
            login(request, user=user) 
            return redirect('/forum/list/')
        else:
            return render(request, 'account/login.html', {'form':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
    


class ProfileView(View):
    def get(self, request):
        user = User.objects.filter(id=request.user.id).last()
        if user:
            return render(
                request,
                'account/profile.html', 
                {
                    'email': user.email,
                    'name': user.name,
                    'date_joined': user.date_joined
                }
            )
        else:
            return render(request, 'account/login.html', {'form': LoginForm()} )