from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']  # 依 id 欄位由大至小排序

# 檢視留言
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    model = Message
    fields = '__all__'
    success_url = '/message/'


