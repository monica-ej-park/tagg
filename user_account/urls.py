from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import SignupView, LoginView, ProfileView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('me/', ProfileView.as_view(), name='me'),
    path('withdrawal/', ProfileView.withdrawal, name='withdrawal'),
    #path('accounts/', include('django.contrib.auth.urls')),
    
    # ??
    #path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user_account/registration/password_reset_form.html'), name='password_reset'),
    #path("password_reset", views.password_reset_request, name="password_reset"),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user_account/registration/password_reset_done.html'), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user_account/registration/password_reset_confirm.html"), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user_account/registration/password_reset_complete.html'), name='password_reset_complete'),      
    
    #path('forgot_email/', views.forgot_email, name="forgot_email"),

    #path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
