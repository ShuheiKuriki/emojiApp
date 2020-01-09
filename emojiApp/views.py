from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'title': "Let's Translate Natural Languages into Emojis!"})

def emoji(request, foo):
    return render(request, 'index.html', {'title': foo})

def render_form(request):
    return render(request, 'login.html')

def login(request):
    if request.POST['username'] and request.POST['email']:
        return render(request, 'check.html', {"email": request.POST['email'], "username": request.POST['username']})
    else:
        return render(request, 'error.html')
