from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'title': "Let's Translate Natural Languages into Emojis!"})