from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    # 로그인이 되어있다면,
    if request.user.is_authenticated:
        return redirect('community:movie_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form = form.save()
            # 게시글 목록 페이지
            auth_login(request, form)
            return redirect('community:movie_list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('community:movie_list')
    if request.method == 'POST':
        # 사용자가 보낸 값 -> form
        form = AuthenticationForm(request, request.POST)
        # 검증
        if form.is_valid():
            # 검증 완료시 로그인!
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:movie_list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    # 조건식으로 직접 작성 해도 된다.
    auth_logout(request)
    return redirect('community:movie_list')



def follow(request, username):
    User = get_user_model()
    # 팔로우 당하는 사람
    user = get_object_or_404(User, username=username)
    if user != request.user:
        # 팔로우를 요청한 사람 => request.user
        # 팔로우가 되어 있다면,
        if user.followers.filter(pk=request.user.pk).exists():
            # 삭제
            user.followers.remove(request.user)
        else:
            # 추가
            user.followers.add(request.user)
    return redirect('accounts:profile', username)

@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)