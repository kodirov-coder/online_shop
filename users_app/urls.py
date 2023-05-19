from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import login_view, UserRegisterView, ProfileUpdateView, logout


urlpatterns = [
    path("login/", login_view, name="login-page"),
    path("register/", UserRegisterView.as_view(), name="register-page"),
    path("profile/<int:pk>/", login_required(ProfileUpdateView.as_view()), name="profile-page"),
    path("logout/", logout, name="logout"),
]