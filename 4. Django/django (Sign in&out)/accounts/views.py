from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.user.is_authenticated:   # 로그인된 유저가 회원가입 링크를 누르면 index페이지로 redirect
        return redirect('accounts:index')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)   # 회원가입 후 자동 로그인 처리
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:   # 로그인된 유저가 로그인 링크를 누르면 index페이지로 redirect
        return redirect('accounts:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('accounts:index')

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/change_password.html', context)

# # UserCreationForm 사용하지 않고 작성 #
# def signup(request):
#     if request.method == "POST":
#         # 회원가입 진행
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         new_user = User.objects.create_user(
#             username = username,
#             password = password,
#         )
#         return redirect('accounts:index')
#     else:
#         # 비어있는 폼 보여주기
#         return render(request, 'accounts/signup.html')

# # AuthenticationForm 사용하지 않고 작성 #
# def login(request):
#     if request.method == "POST":
#         # 로그인 진행
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # 아이디와 비밀번호 일치여부 확인
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('accounts:index')
#         else:
#             error_message = "아이디 또는 비밀번호가 일치하지 않습니다."
#     else:
#         error_message = ""
#     context = {'error_message': error_message}
#     return render(request, 'accounts/login.html', context)