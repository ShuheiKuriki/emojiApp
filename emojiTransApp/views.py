from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sentence_form.html')

def emoji(index):
    return HttpResponse("""
        <!DOCTYPEhtml>
        <html>
            <head>
                <meta charset="utf8"/>
                <link rel="stylesheet" href="/static/style.css"/>
            </head>
            <body>
                <h1>HelloWorld</h1>
            </body>
        </html>
    """)

def search(request):
    q = request.GET.get('q')
    return HttpResponse(q)

def result(request):
    if request.POST['sentence']:
        return render(request, 'result.html', {"sentence": request.POST['sentence']})
    else:
        return render(request, 'error.html')
