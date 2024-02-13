from django.shortcuts import render

def home(request):
    context={}
    return render(request, "Rent/home.html", context)
