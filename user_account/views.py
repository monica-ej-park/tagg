from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login, logout, authenticate 

from .models import User
from django.views import View
from .forms import SignupForm, LoginForm

from django.contrib.auth import views as auth_views


class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/forum/list/')
        
        context = {
            'form': SignupForm()
        }
        return render(request, 'user_account/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            print("form valid")
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
        return render(request, 'user_account/signup.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'user_account/login.html', {'form': LoginForm()} )

    def post(self, request):
        form = LoginForm(request.POST)
        email = request.POST['email']
        pw = request.POST['password']
        user = authenticate(email=email, password=pw)
        if user: 
            login(request, user=user) 
            return redirect('/forum/list/')
        else:
            return render(request, 'user_account/login.html', {'form':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
    


class ProfileView(View):
    def get(self, request):
        user = User.objects.filter(id=request.user.id).last()
        if user:
            return render(
                request,
                'user_account/profile.html', 
                {
                    'email': user.email,
                    'name': user.name,
                    'date_joined': user.date_joined
                }
            )
        else:
            return render(request, 'user_account/login.html', {'form': LoginForm()} )


    def withdrawal(request):
        user = User.objects.filter(id=request.user.id).last()
        if user:
            user.is_active = False
            user.save()
        return redirect('/forum/list/')
    

"""
def forgot_email(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        try:
            user = User.objects.get(id=email)
            if user is not None:
                
        except:

    pass
"""

class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'user_account/registration/password_reset_form.html' #템플릿을 변경하려면 이와같은 형식으로 입력
    title = "비밀번호 변경"

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            opts = {
                'use_https': self.request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.subject_template_name,
                'request': self.request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
            return HttpResponseRedirect(self.get_success_url())
            #return super().form_valid(form) # 이메일 중복발신됨.
        else:
            return render(self.request, 'user_account/registration/password_reset_done_fail.html')


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "user_account/registration/password_reset_done.html"
    title = "비밀번호 변경 URL 전송"


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "user_account/registration/password_reset_confirm.html"


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "user_account/registration/password_reset_complete.html"
    title = "비밀번호 변경 완료"