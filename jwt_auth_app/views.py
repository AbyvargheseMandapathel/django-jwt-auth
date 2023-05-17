from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect, render
from  django.views.generic import TemplateView

class LoginView(APIView):
    def get(self, request):
        # Render the login form
        return render(request, 'login', {})  # Add an empty dictionary as context

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            request.session['token'] = token  # Store the token in the session
            
             # Print statements for debugging
            print(f"User {user.username} successfully logged in")
            print(f"User is authenticated: {user.is_authenticated}")
            
            
            return redirect('/home')
        else:
            return render(request, '/login', {'error': 'Invalid credentials'})

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('/login')

    def post(self, request):
        logout(request)
        return redirect('/login')

class HomeView(APIView):
    def get(self, request):
        token = request.session.get('token')
        username = request.user.username

        # Print statements for debugging
        print(request.headers)
        print("User:", request.user)  # Print the user object
        print("Username:", username)  # Print the username

        data = {
            'username': username,
            'token': token
        }
        return Response(data)


