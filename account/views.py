from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreatUserForm, CustomAuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    form  = CreatUserForm()

    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for ' + user)
            return redirect('account:login')
    context = {'form':form}
    return render(request, 'signup.html', context)
