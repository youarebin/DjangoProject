from django.shortcuts import render, redirect, get_object_or_404 
from blog.models import Post, Comment
from blog.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render

def post(request):
    return render(request, "post.html")

#게시글 목록 조회
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    my_paginator = Paginator(posts, 5)
    page_num = request.GET.get('page')
    posts = my_paginator.get_page(page_num)
    return render(request, "post_list.html", {"posts" : posts})

#게시글 상세페이지 조회
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)

#게시글 수정
def post_update(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:   #GET이면
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'id':id})

#게시글 삭제
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')

#댓글 생성
def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk=id)
        finished_form.save()
    return redirect('post_detail', id)

#댓글 수정
def update_comment(request, post_id, com_id):
    comment = Comment.objects.get(id=com_id)
    
    if request.method == "POST": # 사용자가 수정 후 POST 요청을 보냈을 때
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('post_detail', post_id)
    else: # GET 요청일 때
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'comment_update.html', context)

#댓글 삭제
def delete_comment(request, post_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('post_detail', post_id)