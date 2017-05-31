from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from blog.forms import PostCreatForm
from blog.models import Post


def main_view(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'post/post-list.html' ,context=context)


def post_add_view(request):
    if request.method == "GET":
        form = PostCreatForm()
        context = {
            'form': form
        }
        return render(request, 'post/post-add.html', context=context)

    elif request.method == "POST":
        form = PostCreatForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first().id
            Post.objects.create(author_id=user,title = title, text = text)
            return redirect('main_view')
        else:
            context = {
                'form':form,
            }
            return render(request, 'post/post-add.html',context=context)