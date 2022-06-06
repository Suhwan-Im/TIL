from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 1. 모델을 이용해서 모든 데이터를 가져온다.
    #articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # 2. 가져온 데이터를 템플릿으로 넘긴다.
    context = {'articles': articles}
    # 3. 템플릿에서 데이터를 보여준다.
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 데이터 저장하기
    article = Article(title = title, content = content)
    article.save()

    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        # 1. pk에 해당하는 글을 DB에서 가져온다.
        article = Article.objects.get(pk=pk)
        # 2. 해당 글을 삭제한다.
        article.delete()
        # 3. index 페이지로 이동하게 한다.
        return redirect('articles:index')
    else:
        article = Article.objects.get(pk=pk)
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 수정할 article을 가져온다.
    article = Article.objects.get(pk=pk)
    # 2. request로 부터 사용자가 입력한 데이터를 가져온다.
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. article을 수정한다.
    article.save()
    # 4. article 상세 페이지로 보낸다.
    return redirect('articles:detail', article.pk)
