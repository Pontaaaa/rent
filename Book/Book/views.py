from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse

def sign_in_modal(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in_modal.html', {'form': form})

def sign_up_modal(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse("home"))
    else:
        form = UserCreationForm()
    return render(request, 'sign_up_modal.html', {'form': form})