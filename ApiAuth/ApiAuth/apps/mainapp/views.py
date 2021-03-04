from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

class SignUpApi(APIView):
    def post(self, request):           
        username, email, password = request.data.get("username"), request.data.get("email"), request.data.get("password")
        user = User.objects.create_user(username, email, password)
        if user:
            return Response({"message": "OK"}, status=200)
        else:
            return Response({"message": "ERR"}, status=401)


class SignInApi(APIView):
    def post(self, request):
        username, password = request.data.get("username"), request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "OK"}, status=200)
        else:
            return Response({"message": "ERR"}, status=401)


class MainView(TemplateView):
    template_name = 'ApiAuth/main.html'

class SignInView(TemplateView):
    template_name = 'ApiAuth/sign_in.html'

class SignUpView(TemplateView):
    template_name = 'ApiAuth/sign_up.html'

class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('You are logged out of your account')
