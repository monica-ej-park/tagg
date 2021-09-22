from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import SignupView, LoginView, ProfileView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('me/', ProfileView.as_view(), name='me'),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', views.do_signup, name='signup'),
    # path('login/', views.do_login, name='login'),
    # path('logout/', views.do_logout, name='logout'),
    
]
