from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("", views.home, name="home"),
    path("number_verification/", views.number_verification, name="number_verification"),
    path("otp/", views.otp_verification, name="otp"),
    path("qr_code/", views.qr_gen, name="qr_code"),
    path("upload/", views.face_detect, name="upload"),
    path("verified/", views.verify, name="verified")
]