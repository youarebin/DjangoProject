from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo']  # 입력받을 필드를 정의

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']