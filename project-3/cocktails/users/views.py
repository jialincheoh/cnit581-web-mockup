from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from .models import CheckboxData
from .models import UserInput
from .models import User

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
        checkbox_data = CheckboxData(
            checkbox1=request.POST.get('checkbox1', False),
            checkbox2=request.POST.get('checkbox2', False),
            checkbox3=request.POST.get('checkbox3', False),
            checkbox4=request.POST.get('checkbox4', False),
            checkbox5=request.POST.get('checkbox5', False),
            checkbox6=request.POST.get('checkbox6', False)
        )
        # Check if all checkboxes are checked
        print('all(checkbox_data.values())',all(checkbox_data.values()))
        if all(checkbox_data.values()):
            
            # Save checkbox data
            checkbox_data_object = CheckboxData.objects.create(**checkbox_data)
            checkbox_data_object.save()
            # Redirect to task1 page
            return redirect('/task1')
        else:
            # If not all checkboxes are checked, return an error message
            error_message = "Please check all checkboxes."
            return render(request, 'users/dashboard.html', {'error_message': error_message})
    else:
        return render(request, 'users/dashboard.html')

def save_user_input(request):
    if request.method == 'POST':
        user_input_text = request.POST.get('user_input', '')
        task_number = request.POST.get('task_number', 1)
        user = request.user
        #user = User.objects.get(username=request.user.username)
        print(">>>>", user)
        
        # Save user input to the database
        UserInput.objects.create(
            text=user_input_text,
            task_number=task_number,
            user=user
        )

        # Redirect or render a response as needed
        if int(task_number) == 6:
            return redirect('/final/')    
        return redirect('/task' + str(int(task_number) + 1) + '/')
    else:
        return HttpResponse('Invalid request method.')
    
def task1(request):
    # Your view logic here
    return render(request, 'users/task1.html')

def task2(request):
    # Your view logic here
    return render(request, 'users/task2.html')

def task3(request):
    # Your view logic here
    return render(request, 'users/task3.html')

def task4(request):
    # Your view logic here
    return render(request, 'users/task4.html')

def task5(request):
    # Your view logic here
    return render(request, 'users/task5.html')

def task6(request):
    # Your view logic here
    return render(request, 'users/task6.html')

def final(request):
    # Your view logic here
    return render(request, 'users/final.html')
