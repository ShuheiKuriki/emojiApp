from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'emoji/emoji_top.html')

def form(request):
    return render(request, 'emoji/sentence_form.html')

def result(request):
    import emoji_translate
    if request.POST.get('sentence'):
        sentence = request.POST.get('sentence')
        emojis = translate.phr_to_emojis(sentence)
        emojis2 = translate.phr_to_emoji(sentence,3)
        return render(request, 'emoji/result.html', {"sentence": sentence, "emojis": emojis, "emojis2": emojis2})
    else:
        return render(request, 'error.html')

def visualize(request):
    return render(request, 'emoji/visualize.html')

