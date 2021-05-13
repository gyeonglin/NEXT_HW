from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method=='POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content
        )
        return redirect('detail', post_pk)
    
    return render(request, 'detail.html', {'post' : post})

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def new(request):
    if request.method == 'POST' :
        #POST 요청일 경우
            print(request.POST)
            new_post = Post.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
                deadline = request.POST['deadline']
            )
            return redirect('detail', post_pk=new_post.pk)

    #POST 요청이 아닐 경우
    return render(request, 'new.html')

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post' : post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')