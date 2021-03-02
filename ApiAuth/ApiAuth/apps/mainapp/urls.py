from django.urls import path
from .views import *

app_name = "mainapp"
urlpatterns = [
    path('main/', MainView.as_view()),
    path('sign/in/', SignInView.as_view()),
    path('sign/up/', SignUpView.as_view()),
    path('sign/out/', SignOutView.as_view()),

    path('api/sign/in/', SignInApi.as_view()),
    path('api/sign/up/', SignUpApi.as_view()),
]

