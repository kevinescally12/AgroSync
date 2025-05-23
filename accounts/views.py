# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
            user = form.get_user()
            auth_login(request, user)

            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)

            if user.rol == 'agricultor':
                return redirect('home')
            elif user.rol == 'ingeniero':
                return redirect('home')
            elif user.rol == 'cooperativa':
                return redirect('home')
            else:
                return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')


'''@login_required
def dashboard_agricultor(request):
    #return HttpResponse("Hola agricultor")
    return render(request, 'home.html')

#@login_required
def dashboard_ingeniero(request):
    #return HttpResponse("Hola ingeniero")
    return render(request, 'home.html')

@login_required
def dashboard_cooperativa(request):
    return HttpResponse("home.html")
    #return render(request, 'dashboards/cooperativa.html')'''
