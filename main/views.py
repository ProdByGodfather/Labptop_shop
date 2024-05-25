from django.shortcuts import render
from main import models
from django.http import HttpResponseNotFound

def home(request):
    if request.GET.get('category') and request.GET.get('category') != "":
        category = models.Category.objects.get(id=request.GET.get('category'))
        post = models.Post.objects.filter(category=category)
    else:
        post = models.Post.objects.all().order_by('-create_time')
    context = {
        'post':post
    }
    return render(request, 'home.html', context)


def detail(request, id):
    try:
        i = models.Post.objects.get(id=id)
        context = {
            'i': i
        }
        return render(request, 'detail.html', context)
    except:
        return HttpResponseNotFound("hello")    