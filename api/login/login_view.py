from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages



# Create your views here.
def login_views(request):
    template_name = "login.html"
    
        # Verifica si el usuario ya está autenticado
    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials or user is not active')
    return render(request, template_name)


# registrate kbron
def register_view(request):
    template_name = "registro.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        print(username)
        print(email)
        print(password)
        print(password_confirmation)
        
        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya existe')
            return render(request, template_name)

        user = User(
            username=username,
            email=email,
            password=make_password(password),
            is_active = 0
            
        )
        user.save()
        messages.success(request, 'Cuenta creada exitosamente')
    return render(request,template_name)

# forgot the password
def forgot_view(request):
    template_name = "forgot_pass.html"
    return render(request,template_name)

def logout_view(request):
    logout(request)
    return redirect('login')



