# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.http import is_safe_url
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.conf import settings

from .forms import PaperForm, SortForm
from .models import Paper

from datetime import date

# Create your views here.

def index(request):
    return redirect('paper:list', sort='-edit_date')

class PaperListView(ListView):
    model = Paper

    def get_queryset(self):
        key = self.kwargs['sort']
        papers = Paper.objects.all().order_by(key)
        return papers

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)  #テンプレートに渡すコンテキストに 「user_count」 という変数を追加
            context['form'] = SortForm
            return context

def sort(request):
    if request.method == "POST":
        s = request.POST.get('key')
        return redirect('paper:list', sort=s)
    else:
        return redirect('paper:list', sort='deadline')

class PaperCreateView(CreateView):
    form_class = PaperForm
    template_name = 'paper/paper_create.html'
    success_url = reverse_lazy('paper:index')

class PaperUpdateView(UpdateView):
    model = Paper
    form_class = PaperForm

    def get_success_url(self):
        return reverse_lazy('paper:index')

@require_POST
def delete(request,pk):
    paper = get_object_or_404(Paper, pk=pk)
    paper.delete()
    return redirect('paper:index')

class PaperDetailView(DetailView):
    model = Paper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meta_fields = Paper._meta.get_fields()
        dic = {}
        for field in meta_fields:
            if field.name != 'id':
                exec('dic[field.verbose_name]=context["object"].{}'.format(field.name))
        context['info'] = dic
        return context


def redirect_to_origin(request):
    redirect_to = request.GET.get('next')
    url_is_safe = is_safe_url(
        url=redirect_to,
        allowed_hosts=settings.ALLOWED_HOSTS,
        require_https=request.is_secure(),
    )
    if url_is_safe and redirect_to:
        return redirect(redirect_to)

def original_url(self):
    url = self.request.GET.get('next')
    url_is_safe = is_safe_url(
        url=url,
        allowed_hosts=settings.ALLOWED_HOSTS,
        require_https=self.request.is_secure(),
    )
    if url_is_safe and url:
        return url
