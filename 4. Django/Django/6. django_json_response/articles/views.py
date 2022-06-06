from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer


# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)

# 직접 입력하기
def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'updated_at': article.updated_at,
                'created_at': article.created_at,
            }
        )
    
    return JsonResponse(articles_json, safe=False)

# django.core의 serializers 모듈 이용하기
def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')

 # DRF 이용하기 (serializers.py 직접 구현)
@ api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)