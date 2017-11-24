from django.contrib.auth import login
from django.shortcuts import redirect, render

from members.forms import SignupForm, SigninForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('restaurant-list')
    else:
        form = SignupForm
    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            form.signin(request)
            return redirect('restaurant-list')
    else:
        form = SigninForm
    context = {
        'form': form,
    }
    return render(request, 'members/signin.html', context)
