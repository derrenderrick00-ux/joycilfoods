from django.urls import path
from . import views
from .views import signup_view, profile_edit_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", signup_view, name="signup"),
    path('profile/edit', profile_edit_view, name='profile_edit'),    
    path('verify-email/<int:uid>/<str:token>/', views.verify_email, name='verify_email'),
]
