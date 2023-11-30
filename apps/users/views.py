from django.shortcuts import render, get_object_or_404, redirect

from .models import Users
from .forms import UserForm

# Create your views here.

# create
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

# read
def findUsers(request):
    template_name = 'users/list_users.html'
    users = Users.objects.filter()
    context = {
        'users': users
    }
    return render(request, template_name, context)

# update
def updateUser():
    print()

# delete
def deleteUser():
    print()