from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Review, Comment, Movie
from .forms import ReviewForm, MovieForm
from .forms import CommentForm
from django.db.models import Avg

def comments_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
    return redirect('community:review_detail',review.pk)


def comments_delete(request, review_pk, comment_pk):

    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        if request.user==comment.user: #추가함
            comment.delete()
    return redirect('community:review_detail', review_pk)




#전체 리뷰 목록 조회
def review_list(request):
    reviews = Review.objects.all()
    context ={
        'reviews':reviews
    }
    return render(request, 'community/review_list.html',context)

#신규 리뷰 생성
def review_create(request, movie_pk):
    #POST
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES)

            # 유효성 검사
            if form.is_valid():
                form = form.save(commit=False)
                form.movie = movie
                form.user = request.user
                form.save()
                return redirect('community:movie_detail', movie_pk)

            else:
                return redirect('community:movie_detail', movie_pk)

        #GET    (구 new)

        else :
            form = ReviewForm()
        context = {
            'form': form,
            'movie': movie,
        }
        return render(request,'community/form.html',context)
    else:
        return redirect('accounts:login')


def review_detail(request,pk):
    review= get_object_or_404(Review, pk=pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {

        'review': review,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'community/review_detail.html',context)

def review_update(request,pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:review_detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review' :review,
    }
    return render(request, 'community/form.html', context)

@require_POST
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('community:review_list')

def movie_list(request):
    movies = Movie.objects.all()
    context ={
        'movies': movies,
    }
    return render(request, 'community/movie_list.html',context)


@login_required
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('community:review_list')


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.review_set.all()
    total_rank = 0
    i = 0
    for review in reviews:
        i += 1
        total_rank += review.rank

    if i != 0:
        avg_rank = total_rank / i
    else:
        avg_rank = "작성된 리뷰가 없습니다."

    age_cnt = [0]*7
    male_rank = 0
    female_rank = 0
    male_cnt= 0
    female_cnt = 0
    total_rank = {'10대':0,
        '20대': 0,
        '30대': 0,
        '40대': 0,
        '50대': 0,
        '60대': 0

    }
    for review in reviews:
        if review.user.gender == 'male':
            male_rank += review.rank
            male_cnt +=1
        else:
            female_rank += review.rank
            female_cnt+=1
        for i in range(1, 7):
            if i*10 <= review.user.age < (i+1)*10:
                age_cnt[i] += 1
                if total_rank[f'{i*10}대']:
                    total_rank[f'{i*10}대'] += review.rank
                else:
                    total_rank[f'{i*10}대'] = review.rank
    for i in range(1, 7):
        if age_cnt[i] != 0:
            total_rank[f'{i*10}대'] = total_rank[f'{i*10}대']/age_cnt[i]
        else:
            total_rank[f'{i*10}대'] = 0

    if male_cnt != 0:
        male_rank_avg = male_rank/male_cnt
    else:
        male_rank_avg = 0
    if female_cnt != 0:
        female_rank_avg = female_rank/female_cnt
    else:
        female_rank_avg = 0



    context = {
        'movie': movie,
        'reviews': reviews,
        'rank': avg_rank,
        'male_rank': male_rank_avg,
        'female_rank': female_rank_avg,
        'total_rank': total_rank,

    }
    return render(request, 'community/movie_detail.html',context)

@login_required
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('community:review_detail', review_pk)


def movie_create(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                form = form.save()
                return redirect('community:movie_list')
            else:
                return redirect('community:movie_list')
        else :
            form = MovieForm()
        context = {
            'form': form,

        }
        return render(request,'community/form.html',context)
    else:
        return redirect('accounts:login')


@login_required
def movie_update(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('community:movie_detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,

    }
    return render(request, 'community/form.html', context)

@require_POST
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('community:movie_list')
