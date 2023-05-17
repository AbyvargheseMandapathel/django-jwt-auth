from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            request.session['token'] = token  # Store the token in the session
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

    def post(self, request):
        logout(request)
        return redirect('login')

class HomeView(View):
    def get(self, request):
        token = request.session.get('token')  # Retrieve the token from the session
        username = request.user.username
        return render(request, 'home.html', {'username': username, 'token': token})

