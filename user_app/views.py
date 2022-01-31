from django.shortcuts import render

def login(request):
    return render(request, 'user_app/login.html')


def register(request):
    return render(request, 'user_app/register.html')