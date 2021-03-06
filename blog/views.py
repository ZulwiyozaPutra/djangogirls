from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, primary_key):
    post = get_object_or_404(Post, pk=primary_key)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publication_date = timezone.now()
            post.save()
            return redirect('post_detail', primary_key=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, primary_key):
    post = get_object_or_404(Post, pk=primary_key)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publication_date = timezone.now()
            post.save()
            return redirect('post_detail', primary_key=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})