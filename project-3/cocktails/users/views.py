from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('experiment-dashboard')
    else: 
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
