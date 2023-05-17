from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import auth, messages

def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username=form['username'].value()
            password=form['password'].value()

            user = auth.authenticate(
                    request,
                    username=username,
                    password=password
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, f"{username} logado com sucesso!")
                return redirect('home')
            
            messages.error(request, "Erro ao efetuar login")
            return redirect('login')
    return render(request, "users/login.html", {"form": form})

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Registrado com sucesso." )
            return redirect('login')
        else:
            messages.error(request, "Não foi possível registrar. Verifique os dados e tente novamente.")

    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso.')
    return redirect('login')