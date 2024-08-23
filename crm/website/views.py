from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect(request, 'website/home.html', {})
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect('home')
    else:
        return render(request, 'website/home.html')
        
    return render(request, 'website/home.html', {})



def logout_user(request):
    pass


# Heading to Logout