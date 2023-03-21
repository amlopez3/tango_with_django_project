from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'news/index.html', context=context_dict)

