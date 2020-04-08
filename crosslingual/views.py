from django.shortcuts import render, redirect
# Create your viewfrom django.shortcuts import render
from django.http import HttpResponse
from cross_translate import translate
from .forms import TranslateForm
from .models import Translate
import os

# Create your views here.
def index(request):
    return render(request, 'crosslingual/cross_top.html')

def form(request):
    form = TranslateForm()
    return render(request, 'crosslingual/cross_form.html', {'form' : form})

def result(request):
    if request.method != 'POST':
        return redirect(to='/form')
    form = TranslateForm(request.POST)
    if form.is_valid():
        src_word = request.POST.get('source')
        src_tgt_lang = request.POST.get('src_tgt_lang')
        src_lang, tgt_lang = src_tgt_lang.split('-')
        src_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src_lang, tgt_lang, src_lang)
        tgt_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src_lang, tgt_lang, tgt_lang)
        src_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src_lang, tgt_lang, src_lang)
        tgt_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src_lang, tgt_lang, tgt_lang)
        src_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src_lang, tgt_lang, src_lang)
        tgt_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src_lang, tgt_lang, tgt_lang)
        nmax = 50000
        # print("OK1")
        try:
            tgt_sup_words = [str(i) for i in translate(src_sup_path, tgt_sup_path, nmax, src_word)]
        except:
            tgt_sup_words = ["" for i in range(5)]
        # print("OK2")
        try:
            tgt_unsup_words = [str(i) for i in translate(src_unsup_path, tgt_unsup_path, nmax, src_word)]
        except:
            tgt_unsup_words = ["" for i in range(5)]
        print("OK3")
        try:
            tgt_joint_words = [str(i) for i in translate(src_joint_path, tgt_joint_path, 250000, src_word)]
        except:
            print("OK6")
            tgt_joint_words = ["" for i in range(5)]
            # print("OK7")
        # print("OK8")
        Translate.objects.create(
            source=src_word,
            target_sup=tgt_sup_words,
            target_unsup=tgt_unsup_words,
            target_joint=tgt_joint_words,
            src_tgt_lang=src_tgt_lang
        )
        # print("OK9")
        return render(request, 'crosslingual/cross_result.html', {"source":src_word, "lang": {'src':src_lang,'tgt':tgt_lang}, "targets": {"sup":tgt_sup_words, "unsup":tgt_unsup_words, "joint":tgt_joint_words}})
    else:
        return render(request, 'error.html')

def translate_list(request):
    translates = Translate.objects.all()
    return render(request, 'crosslingual/translate_list.html', {'trans':translates})

def visual(request):
    return render(request, 'visualize_form.html')
