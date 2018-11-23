from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from mysite.forms import SignUpForm, LoginForm


def mainPage(request):
    return render(request, 'mainPage.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm()
    return render(request, 'registerPage.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        #if form.is_valid():
        print("salam")
        #form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('main_page')
    else:
        form = LoginForm()
    return render(request, 'loginPage.html', {'form': form})
