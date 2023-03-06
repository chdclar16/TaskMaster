from django.urls import path

from accounts.views import login_user, logout_user, signup_user

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("signup/", signup_user, name="signup"),
]
