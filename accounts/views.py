# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado con éxito. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Autentica al usuario
            user = form.get_user()
            auth_login(request, user)  # Importar desde django.contrib.auth
            
            # Maneja el "remember me"
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)  # Sesión expira al cerrar navegador
            
            return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')
