from django.shortcuts import render
from news.models import New

def index(request):
    news_list = New.objects.all()

    context_dict = {}

    context_dict['news'] = news_list

    return render(request, 'news/index.html', context=context_dict)

