from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user}!')
            login(request, user)
            return render(request, 'users/dashboard.html')
    else: 
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        # Authenticate
        form = AuthenticationForm(request, request.POST)
        print('form valid', form.is_valid())
        print(form.errors)
        #print('username', form.cleaned_data.get('username'))
        #print('password', form.cleaned_data.get('password'))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('user object', user)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return render(request, 'users/dashboard.html')
            else:
                messages.error(request, 'Invalid username or password.')
        else: 
             messages.error(request, 'Wrong credential!')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def dashboard(request):
    if request.method == 'POST':
        # Process form data here
        # You can access form data using request.POST.get('checkbox1'), etc.
        return HttpResponse('Form submitted successfully!')
    else:
        return render(request, 'dashboard.html')
