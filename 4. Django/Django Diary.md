# Django Diary

## (Model Form)



### 1. Django 설치하기

- 가상환경 생성

![image-20220302093424697](Django%20Diary.assets/image-20220302093424697.png)

- Django 3.2.12버전 설치

![image-20220302094123261](Django%20Diary.assets/image-20220302094123261.png)

- 프로젝트 생성

![image-20220302094716908](Django%20Diary.assets/image-20220302094716908.png)

- Django 서버 시작하기 (Ctrl+C로 종료)

![image-20220302100935132](Django%20Diary.assets/image-20220302100935132.png)

- Application 생성

![image-20220302101113305](Django%20Diary.assets/image-20220302101113305.png)



### 2. settings.py

- INSTALLED_APPS에 application 추가

  ```py
  INSTALLED_APPS = [
      'articles',		# application 추가
      'django.contrib.admin',
      ...
  ]
  ```

- TEMPLATES에 DIRS 설정

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          ...
      }
  ]



### 3. models.py

- 필요한 항목들을 생성

  ```python
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```

- Migration 진행 (models.py에 새로운 항목이 추가되면 아래의 1~2번 반복해서 다시 적용해주기)

  1. Migration 만들기: `python manage.py makemigrations`
  2. Migration 적용하기: `python manage.py migrate`
  3. SQL 변환 코드 보기: `python manage.py sqlmigrate <app_name> <no.>`
  4. migration 적용여부 보기: `python manage.py showmigrations` (`[X]`표시가 적용됨을 의미)

- forms.py (models.py와 같은 형식으로 만들기도 함)

  ```python
  from django import forms
  from articles.models import Article
  
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- Admin.py 작성하기

  - `python manage.py createsuperuser` 명령어로 admin 계성 생성
  - 그 후, Admin.py에 아래의 코드를 작성

  ```python
  from django.contrib import admin
  from .models import Article
  
  # Register your models here.
  admin.site.register(Article)
  ```



### 4. urls.py

- 프로젝트 내에 위치한 url.py 파일

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ]
  ```

- 어플리케이션 내에 위치한 url.py 파일

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/delete/', views.delete, name='delete'),
      path('<int:pk>/update/', views.update, name='update'),
  ]
  ```



### 5. views.py

- Model Form 사용시

  ```python
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleForm
  
  # Create your views here.
  def index(request):
      articles = Article.objects.all()[::-1]
      context = {'articles': articles}
      return render(request, 'articles/index.html', context)
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
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
  ```



### 6. html 파일들

- base.html (프로젝트 폴더와 동일 선상에 위치한 templates 폴더내에 작성)

  ```python
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Django CRUD PJT</title>
  </head>
  <body>
    <div class="container">
      {% block content %}
      {% endblock content %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

- index.html

  ```python
  {% extends 'base.html' %}
  
  {% block content %}
    <h1 class="text-center">글 목록</h1>
    <a href={% url 'articles:create' %}>[글 작성]</a>
    <hr>
  
    {% for article in articles %}
      <p>글 번호: {{ article.pk }}</p>
      <a href={% url 'articles:detail' article.pk %}>글 제목: {{ article.title }}</a>   <!-- 'article.pk'를 뒤에 붙여서 같이 넘겨주기 -->
      <p>글 내용: {{ article.content }}</p>
      <hr>
    {% endfor %}
  {% endblock content %}
  ```

- create.html

  ```python
  {% extends 'base.html' %}
  
  {% block content %}
    <h1 class="text-center">CREATE</h1>
  
    <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
  
      <input type="submit">
    </form>
  
    <a href={% url 'articles:index' %}>[글 목록]</a>
  {% endblock content %}
  ```

- detail.html

  ```python
  {% extends 'base.html' %}
  
  {% block content %}
    <h1 class="text-center">상세 페이지</h1>
    <hr>
  
    <h3>{{article.pk}}번째 글</h3>
    <hr>
    <p>제목: {{article.title}}</p>
    <p>내용: {{article.content}}</p>
    <p>작성 시간: {{article.created_at}}</p>
    <p>수정 시간: {{article.updated_at}}</p>
    <hr>
    <a href={% url 'articles:index' %}>[글 목록]</a>
    <a href={% url 'articles:update' article.pk %}>[글 수정]</a>
    <form action={% url 'articles:delete' article.pk %} method="POST">   <!--form을 사용해서 POST방식으로 조작-->
      {% csrf_token %}
      <button class='btn btn-danger'>글 삭제</button>
    </form>
  {% endblock content %}
  ```

- update.html (create.html과 동일하나 value 값을 적용해줘야 함)

  ```python
  {% extends 'base.html' %}
  
  {% block content %}
    <h1 class="text-center">글 수정</h1>
  
    <form action={% url 'articles:update' article.pk %} method="POST">
      {% csrf_token %}
      {{form.as_p}}
  
      <input type="submit">
    </form>
  
    <a href={% url 'articles:index' %}>[글 목록]</a>
  {% endblock content %}
  ```
