from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def ourworks(request):
    return render(request,"ourworks.html")
