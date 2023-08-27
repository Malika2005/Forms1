from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post

def show_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context)

def show_post(request, pk):
    context = context = {'post': get_object_or_404(Post, pk=pk)}
    return render(request, 'post_detail.html', context)

def create_post(request):
    posts_ = Post.objects.all()
    context = {'posts': posts_}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            pass
            return redirect('posts')
        else:
            context['form'] = form
            return render(request, 'create_post.html', context)
    else:
        context['form'] = PostForm()
        return render(request, 'create_post.html', context)

def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes += 1
    post.save()
    return redirect('posts')
