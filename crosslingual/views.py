from django.shortcuts import render, redirect
# Create your viewfrom django.shortcuts import render
from django.http import HttpResponse
from cross_translate import translate
from .forms import TranslateForm, LangForm, SimilarForm
from .models import Translate, FrequentTable
import os, pickle

langs = {"ja":"日本語", "en":"英語", "es":"スペイン語", "it":"イタリア語", "fr":"フランス語", 
          "pt":"ポルトガル語", "nl":"オランダ語", "ru":"ロシア語", "la":"ラテン語", 
          "eo":"エスペラント語", "zh":"中国語", "ko":"韓国語", "th":"タイ語"}
# Create your views here.
def index(request):
  return render(request, 'crosslingual/cross_top.html')

def form(request):
  form1 = TranslateForm()
  form2 = SimilarForm()
  return render(request, 'crosslingual/cross_form.html', {'form1' : form1, 'form2' : form2})

def result(request):
  if request.method != 'POST':
    return redirect(to='/form')
  form = TranslateForm(request.POST)
  if form.is_valid():
    src_word = request.POST.get('source').lower()
    src_lang = request.POST.get('src_lang')
    tgt_lang = request.POST.get('tgt_lang')
    folder = 'pickle_emb/{}-{}-unsup/'.format(src_lang, tgt_lang)
    if not os.path.exists(folder):
      folder = 'pickle_emb5000/{}-{}-unsup/'.format(src_lang, tgt_lang)
    with open(folder+"src_word2id", 'rb') as f:
      word2id = pickle.load(f)
    if src_word not in word2id:
      tgt_unsup_words = ["入力した単語はリストに存在しません"]
      return render(request, 'crosslingual/cross_result.html', {"source":src_word, "lang": {'src':langs[src_lang],'tgt':langs[tgt_lang]}, "targets": {"unsup":tgt_unsup_words}})
    # src_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src_lang, tgt_lang, src_lang)
    # tgt_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src_lang, tgt_lang, tgt_lang)
    # src_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src_lang, tgt_lang, src_lang)
    # tgt_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src_lang, tgt_lang, tgt_lang)
    # src_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src_lang, tgt_lang, src_lang)
    # tgt_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src_lang, tgt_lang, tgt_lang)
    # try:
    #   tgt_sup_words = [str(i) for i in translate(src_sup_path, tgt_sup_path, nmax, src_word)]
    # except:
    #   tgt_sup_words = ["" for i in range(5)]
    try:
      tgt_unsup_words = [str(i) for i in translate(src_lang, tgt_lang, src_word=src_word)]
    except:
      tgt_unsup_words = ["" for i in range(5)]
    # try:
    #   tgt_joint_words = [str(i) for i in translate(src_joint_path, tgt_joint_path, 250000, src_word)]
    # except:
    #   tgt_joint_words = ["" for i in range(5)]
    # Translate.objects.create(
      # source=src_word,
      # target_sup=tgt_sup_words,
      # target_unsup=tgt_unsup_words,
      # target_joint=tgt_joint_words,
      # src_tgt_lang=src_tgt_lang
    # )
    return render(request, 'crosslingual/cross_result.html', {"source":src_word, "lang": {'src':langs[src_lang],'tgt':langs[tgt_lang]}, "targets": {"unsup":tgt_unsup_words}})
  else:
    return render(request, 'error.html')

def similar_result(request):
  if request.method != 'POST':
    return redirect(to='/form')
  form = SimilarForm(request.POST)
  if form.is_valid():
    src_word = request.POST.get('word')
    try:
      src_word.lower()
    except:
      pass
    src_lang = request.POST.get('lang')
    folder = 'pickle_emb/{}-{}-unsup/'.format(src_lang, src_lang)
    if not os.path.exists(folder):
      folder = 'pickle_emb5000/{}-{}-unsup/'.format(src_lang, src_lang)
    with open(folder+"src_word2id", 'rb') as f:
      word2id = pickle.load(f)
    print(src_word)
    if src_word not in word2id:
      similar_words = ["入力した単語はリストに存在しません"]
      return render(request, 'crosslingual/similar_result.html', {"source":src_word, "lang":langs[src_lang], "results":similar_words})
    # src_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src_lang, tgt_lang, src_lang)
    # tgt_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src_lang, tgt_lang, tgt_lang)
    # src_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src_lang, tgt_lang, src_lang)
    # tgt_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src_lang, tgt_lang, tgt_lang)
    # src_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src_lang, tgt_lang, src_lang)
    # tgt_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src_lang, tgt_lang, tgt_lang)
    # try:
    #   tgt_sup_words = [str(i) for i in translate(src_sup_path, tgt_sup_path, nmax, src_word)]
    # except:
    #   tgt_sup_words = ["" for i in range(5)]
    try:
      similar_words = [str(w) for w in translate(src_lang, src_lang, src_word=src_word)]
    except:
      similar_words = ["" for i in range(10)]
    # try:
    #   tgt_joint_words = [str(i) for i in translate(src_joint_path, tgt_joint_path, 250000, src_word)]
    # except:
    #   tgt_joint_words = ["" for i in range(5)]
    # Translate.objects.create(
      # source=src_word,
      # target_sup=tgt_sup_words,
      # target_unsup=tgt_unsup_words,
      # target_joint=tgt_joint_words,
      # src_tgt_lang=src_tgt_lang
    # )
    return render(request, 'crosslingual/similar_result.html', {"source":src_word, "lang": langs[src_lang], "results": similar_words})
  else:
    return render(request, 'error.html')

def translate_list(request):
  translates = Translate.objects.all()
  return render(request, 'crosslingual/translate_list.html', {'trans':translates})

def frequent_table(request,src,tgt):
  ftable = FrequentTable.objects.filter(src_lang=src, tgt_lang=tgt).order_by('num')
  form = LangForm
  return render(request, 'crosslingual/frequent_table.html', {'ftable':ftable, 'form':form, 'src':langs[src], 'tgt':langs[tgt]})

def transition(request):
  if request.method == "POST":
    s = request.POST.get('src_lang')
    t = request.POST.get('tgt_lang')
    return redirect('crosslingual:table',src=s,tgt=t)
  else:
    return redirect('crosslingual:table',src='en',tgt='es')

def visual(request):
  return render(request, 'visualize_form.html')

def make_table(request):
  src_lang = 'en'
  tgt_lang = 'ja'
  folder = 'pickle_emb/{}-{}-unsup/'.format(src_lang, tgt_lang)
  if not os.path.exists(folder):
    folder = 'pickle_emb5000/{}-{}-unsup/'.format(src_lang, tgt_lang)
  with open(folder+"src_id2word", 'rb') as f:
    src_id2word = pickle.load(f)
  # lists = []
  for i in range(100):
    ans = translate(src_lang, tgt_lang, src_id2word[i])
    dists = [0]*10
    words = [0]*10
    for j,s in enumerate(ans):
      dists[j], words[j] = s.split(' - ')
    # lists.append(src_id2word[i])
    FrequentTable.objects.create(
      num = i,
      source = src_id2word[i],
      words = words,
      dists = dists,
      src_lang = src_lang,
      tgt_lang = tgt_lang
    )
  # print(*lists, sep='\n')
  return render(request, 'crosslingual/cross_top.html')
