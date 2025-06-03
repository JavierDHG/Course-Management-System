from django.shortcuts import render
from .models import Usuarios
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from pages.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.
def index(request):
    courses = Course.objects.all()
    categories = Course.objects.values_list('category', flat=True).distinct()
    return render(request, 'index/index.html', {
        'title': 'Home',
        'user': request.user,
        'courses': courses,
        'categories': categories
        })

def category_courses(request, category):
    courses = Course.objects.filter(category=category)
    return render(request, 'courses/category_courses.html', {
        'title': f'Cursos en {category}',
        'courses': courses,
    })

def login_view(request):
    categories = Course.objects.values_list('category', flat=True).distinct()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Usuarios.objects.filter(email=email).first()
        
        if user and user.check_password(password):
            login(request, user)
            return redirect('index')
        
        return render(request, 'login/login.html', {
            'title': 'Login',
            'error': 'Contraseña o email incorrectos.',
        })
    return render(request, 'login/login.html', {
        'title': 'Login',
        'categories': categories,
    })

def register_view(request):
    categories = Course.objects.values_list('category', flat=True).distinct()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        usuario = Usuarios(
            username=username,
            email=email,
        )
        usuario.set_password(password)
        usuario.save()
        return render(request, 'login/login.html', {
            'title': 'Login',
        })
        

    return render(request, 'register/register.html', {
        'title': 'Registro',
        'categories': categories,
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

@login_required
def update_profile(request):
    user = request.user
    categories = Course.objects.values_list('category', flat=True).distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user.username = username
        user.email = email

        if password:
            user.set_password(password)
            update_session_auth_hash(request, user)

        try:
            user.save()
            messages.success(request, 'Perfil actualizado correctamente.')
        except Exception as e:
            messages.error(request, f'Error al actualizar: {e}')

        return redirect('update_profile')

    return render(request, 'profile/profile.html', {
        'title': 'Actualizar Perfil',
        'categories': categories
    })
