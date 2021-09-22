from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):
    email = forms.CharField(required=True, label='Email')

    class Meta:
        model = User
        #widgets = {'password':forms.PasswordInput}
        field = ['email','password']

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

    def save(self, commit=True): 
        user = super(SignupForm, self).save(commit=False) 
        user.email = self.cleaned_data["email"]
        #user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user