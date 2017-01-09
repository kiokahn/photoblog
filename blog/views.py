from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import Form, CommentForm

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list':post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {
        'post':post,
    })

def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_from_comment.html', {'form':form})

def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_from_comment.html', {'form':form})

def post_new(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'blog/post_from.html', {'form':form})
