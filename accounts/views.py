from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('some_view_after_login')  # change this to your desired redirect
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'accounts/login.html')
