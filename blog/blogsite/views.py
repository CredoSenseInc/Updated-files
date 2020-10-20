from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment


# Create your views here


def index(request):
    s = Comment.objects.get(id__exact= 2)
    return HttpResponse('Hello,' + s.name + ' ' + s.email )
def individual_post(request):
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ': ' + recent_post.content)
