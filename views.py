from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-data_criacao')

    return render(request, 'core/home.html', {'posts': posts})