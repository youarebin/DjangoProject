# Create your views here.
from django.shortcuts import render, redirect
from .forms import PostModelForm

def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST,  request.FILES)  # 입력된 데이터를 form에 저장
        if form.is_valid():  # 폼이 유효한지 검사
            # form.save() #form 데이터를 db에 저장
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')  # 홈으로 리다이렉트
    else:
        form = PostModelForm()  # GET 요청일 경우 빈 폼을 전달
    return render(request, 'form_create.html', {'form': form})