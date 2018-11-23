from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from collection.forms import ContactForm

# Create your views here.
from mysite.forms import SignUpForm


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


def contact(request):
    form_class = ContactForm

    return render(request, 'contact_us_page.html', {
        'form': form_class,
    })
