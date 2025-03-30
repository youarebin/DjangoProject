# Create your views here.
from django.shortcuts import render, redirect
from .forms import PostModelForm

def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)  # 입력된 데이터를 form에 저장
        if form.is_valid():  # 폼이 유효한지 검사
            form.save()  # DB에 저장
            return redirect('home')  # 홈으로 리다이렉트
    else:
        form = PostModelForm()  # GET 요청일 경우 빈 폼을 전달
    return render(request, 'form_create.html', {'form': form})