from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, primary_key):
    post = get_object_or_404(Post, pk=primary_key)
    return render(request, 'blog/post_detail.html', {'post': post})