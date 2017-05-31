from django.shortcuts import render, HttpResponse
# Create your views here.
from blog.models import Post


def main_view(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'blog/base.html',context=context)

