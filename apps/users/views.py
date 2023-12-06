from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Users
from .forms import UserForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("Ouve um erro ao fazer login, tente novamente."))
            return redirect('users:login')
    else:
        template_name = 'users/login.html'
        context = {}
        return render(request, template_name, context)

def add_user(request):
    template_name = 'users/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('users:list_users')
    form = UserForm()
    context['formuser'] = form
    return render(request, template_name, context)


def list_users(request):
    template_name = 'users/list_users.html'
    users = Users.objects.filter()
    context = {
        'users': users
    }
    return render(request, template_name, context)


def edit_user(request, id_user):
    template_name = 'users/add_user.html'
    context = {}
    user = get_object_or_404(Users, id=id_user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,  instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:list_users')
    form = UserForm(instance=user)
    context['formuser'] = form
    return render(request, template_name, context)


def delete_user(request, id_user):
    print(id_user)
    user = Users.objects.get(id=id_user)
    user.delete()
    return redirect('users:list_users')
