from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Memo


# 방법1. - Middleware사용하기
def MiddlewareList(request):
    return Memo.objects.order_by('-id')[:5]

# 방법2-1. - ListView사용하기
# paginate_by : 한페이지에 보여지는 데이터 갯수
#  예) http://localhost:8000/testmiddleware/memo_list.html/?page=1
PageListView = ListView.as_view(model=Memo,
                                paginate_by=2,
                                template_name='testmiddleware/memo_list.html/',
                                context_object_name='memo_list')
# 방법2-2. - DetailView사용하기
PageDetailView = DetailView.as_view(model=Memo,
                                    template_name='testmiddleware/memo_detail.html/')
