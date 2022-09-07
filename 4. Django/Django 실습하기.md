# Django 실습하기



### 프로젝트 생성 후 Veiw와 Template 작성

- Git Bash에서 작성 (프로젝트를 진행할 폴더를 만든 후 안에서 Git Bash 실행)

```bash
# 가상환경 생성
python -m venv venv
source venv/Scripts/activate

# Django 설치 및 확인
pip install django==3.2.12
pip list

# 프로젝트 생성
django-admin startproject <pjt_name> .
```



- VS Code에서 작성 (Git Bash를 실행했던 디렉토리에서 VS Code 실행)

```bash
# ctrl + shift + ` 를 통해 터미널 실행 후 Git Bash 선택
# (venv)가 활성화 안 되어있을 경우
source venv/Scripts/activate

# 서버 실행 (ctrl + c 로 종료)
python manage.py runserver

# Application 생성
python manage.py startapp <app_name>
```



- 프로젝트 내 settings.py
  - line 33 - INSTALLED_APPS에 <app_name> 추가
  - line 107 - LANGUAGE_CODE를 'ko-kr' 로 수정
  - line 109 - TIME_ZONE을 'Asia/Seoul'로 수정



- 프로젝트 내 <app_name> 폴더안에 templates 폴더 생성
  - templates 폴더 안에 어플리케이션과 같은 이름의 <app_name> 폴더 생성
  - 이 곳이 html 파일들을 넣어주는 곳
  - index.html 파일 생성 후 `<h1>Hello!</h1>` 작성



- 프로젝트 내 urls.py
  - line 18 - `from <app_name> import views` 작성
  - line 22 - `path('<app_name>/', views.index, name='index')` 작성



- <app_name>폴더 내 views.py

  - line 4 - 아래 코드 작성

    ```python
    def index(request):
        return render(request, '<app_name>/index.html')
    ```

    

- 터미널의 Git Bash 창에서 `python manage.py runserver` 실행 후 local 웹 접속
  - url을 타고 들어가서 "Hello!" 확인



### Model 작성 후 Migrate 하기

- <app_name>폴더 내 models.py (DB와의 연결창구)

```python
# 모델 예시
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
```



- 터미널의 Git Bash 창

  - Migration 만들기 : `python manage.py makemigrations`
  - Migration 적용하기 : `python manage.py migrate`
  - SQL 변환 코드 보기 : `python manage.py sqlmigrate <app_name> <no.>`
  - migration 적용여부 보기 : `python manage.py showmigrations` (`[X]`표시가 적용됨을 의미)
  - 라이브러리 설치 1 : `pip install ipython`

  - 라이브러리 설치 2 :`pip install django-extensions`
    - 프로젝트 내 settings.py에 INSTALLED_APPS에 'django_extensions' 추가
  - ORM 창 열기 : `python manage.py shell_plus`



- 터미널의 Git Bash내 shell_plus 창

  - Create

    1. 인스턴스를 만들고 save 하는 방법
       - article = Article()
         article.title = "~~"
         article.save()
    2. Keyword 인자를 넘기는 방법
         - article = Article(title = "~~", content = "...")
           article.save()

    3. create() 이용하는 방법
       - Article.objects.create(title = "~~", content = "...")     <--  save()가 필요 없음

  - Read

    1. all: `article = Article.objects.all()`
    2. get(): `article = Article.objects.get(<조건식>)` - 1가지 항목만 반환 필수
       - 가능 조건식: `id=1`, `pk=3`, `title="첫번째 글"` 등 ..
    3. filter(): `article = Article.objects.filter(<조건식>)` - 여러개의 항목 반환 가능
       - 가능 조건식: `title="첫번째 글"`, `title__contains="글"` 등 ..

  - Update

    1. article 변수에 업데이트할 항목을 저장한 후에 `article.title = "네번째 글"`과 같이 사용 

  - Delete

    1. delete(): article 변수에 지울 항목을 저장한 후에 `article.delete()` 코드 사용



### Admin Site 계정 생성

- 터미널의 Git Bash 창
  - `python manage.py createsuperuser`의 명령어로 admin 아이디와 패스워드 생성