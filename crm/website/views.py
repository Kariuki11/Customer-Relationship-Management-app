from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()
    # Check to see if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')  # Redirects to the 'home' URL pattern
        else:
            messages.error(request, "There was an error logging in, please try again")
            return redirect('home')  # Redirects to the 'home' URL pattern
    else:
        return render(request, 'website/home.html', {'records':records})  # Render the template for GET requests



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate & Login.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'website/register.html', {'form':form})
    
    return render(request, 'website/register.html', {'form':form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'website/record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You Must Be Logged In To View Customer Records')
        return redirect('home')































































# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# def home(request):
#     # Check to see if logging in 
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You have successfully logged in')
#             return redirect(request, 'website/home.html', {})
#         else:
#             messages.success(request, "There Was An Error Logging In, Please Try Again")
#             return redirect('home')
#     else:
#         return render(request, 'website/home.html')
        
#     return render(request, 'website/home.html', {})



# def logout_user(request):
#     logout(request)
#     messages.success(request, "You have een logged out ...")
#     return redirect('home')


# # Heading to Logout

# Line 1 to line 26.