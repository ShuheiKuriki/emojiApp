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

from .forms import MemoForm
from .models import Memo

from datetime import date

# Create your views here.

class MemoListView(ListView):
    model = Memo

    def get_queryset(self):
        return Memo.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  #テンプレートに渡すコンテキストに 「user_count」 という変数を追加
        memo_list = context['memo_list']
        col1, col2 = [], []
        for i, memo in enumerate(memo_list):
            if i%2==0:
                col1.append(memo)
            else:
                col2.append(memo)
        context['memo2'] = [col1,col2]
        return context

class MemoCreateView(CreateView):
    form_class = MemoForm
    template_name = 'memo/memo_create.html'
    success_url = reverse_lazy('memo:index')

class MemoUpdateView(UpdateView):
    model = Memo
    form_class = MemoForm

    def get_success_url(self):
        return reverse_lazy('memo:index')

@require_POST
def delete(request,pk):
    memo = get_object_or_404(Memo, pk=pk)
    memo.delete()
    return redirect('memo:index')

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
