from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'emoji_top.html')

def form(request):
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
    import translate
    if request.POST.get('sentence'):
        sentence = request.POST.get('sentence')
        emojis = translate.phr_to_emojis(sentence)
        emojis2 = translate.phr_to_emoji(sentence,3)
        return render(request, 'result.html', {"sentence": sentence, "emojis": emojis, "emojis2": emojis2})
    else:
        return render(request, 'error.html')
