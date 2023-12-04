from django.urls import path
from .views import user_login, user_logout, sign_up

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", sign_up, name="signup"),
]
