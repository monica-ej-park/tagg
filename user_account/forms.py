from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User



#class SocialLoginForm(allauth.account.forms.LoginForm):
#    def login(self, *args, **kwargs):
#       return super(MyCustomLoginForm, self).login(*args, **kwargs)
        

class LoginForm(AuthenticationForm):
    email = forms.CharField(required=True, label='Email')

    class Meta:
        model = User
        #widgets = {'password':forms.PasswordInput}
        field = ['email', 'password']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class SignupForm(UserCreationForm): 
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].help_text = '가입시에만 쓰이는 이름입니다.'
        self.fields['email'].help_text = '가입시 사용자 구분을 위해서 사용됩니다.'
        self.fields['password1'].help_text = '8자리 이상의 영문,특수문자,숫자 혼합 입니다. (숫자만 8자리 X)'
        self.fields['password2'].help_text = '비밀번호 확인을 위해 동일한 비밀번호를 넣어주세요.'


    def save(self, commit=True): 
        user = super(SignupForm, self).save(commit=False) 
        user.email = self.cleaned_data["email"]
        #user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    