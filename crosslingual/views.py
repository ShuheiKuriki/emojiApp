from django.shortcuts import render
# Create your viewfrom django.shortcuts import render
from django.http import HttpResponse
from cross_translate import translate
# Create your views here.
def index(request):
    return render(request, 'cross_top.html')

def form(request):
    return render(request, 'cross_form.html')

def result(request):
    if request.POST.get('en'):
        src_word = request.POST.get('en')
        src_path = 'vectors/en-es-super/vectors-en.txt'
        tgt_path = 'vectors/en-es-super/vectors-es.txt'
        nmax = 50000
        tgt_words = translate(src_path, tgt_path, nmax, src_word)
        return render(request, 'cross_result.html', {"en":src_word, "tgt_words": tgt_words})
    else:
        return render(request, 'error.html')

def visual(request):
    return render(request, 'cross_top.html')
