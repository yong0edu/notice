from django.shortcuts import render
from .models import Notice


def index(request):
    notice = Notice.objects.all()
    return render(request, 'app/index.html',
                  {'list': notice})

def detail(request, num):
    # item = Notice.objects.get(pk=1)
    item = Notice.objects.get(id=num)
    return render(request, 'app/detail.html', {'item':item})