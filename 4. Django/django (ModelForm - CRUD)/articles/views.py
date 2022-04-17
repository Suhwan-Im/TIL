from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# def new(request):
#     form = ArticleForm()
#     context = {'form': form}
#     return render(request, 'articles/new.html', context)
# (create 함수와 병합함)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # ArticleForm을 사용한 위의 한 줄이 아래의 세줄과 같음
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title = title, content = content)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk) # 앱 이름과 별명으로 'articles/detail/'대체 + 'article.pk'도 함께 전송
    else:
        form = ArticleForm()
    
    context = {'form': form}
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)
# (update 함수와 병합함)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article':article}
    return render(request, 'articles/update.html', context)