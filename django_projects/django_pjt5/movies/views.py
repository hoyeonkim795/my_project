from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Genre, Movie
from .forms import MovieForm

# movie_list
# movie_create
# movie_like
# movie_detail

def movie_list(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    user = request.user
    if user.is_authenticated:
        user_genre = int(user.genre)
    else:
        user_genre = 0
    context ={
        'movies' : movies,
        'page_obj': page_obj,
        'user_genre': user_genre,
    }
    return render(request, 'movies/movie_list.html', context)


def movie_create(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                form = form.save()
                return redirect('movies:movie_list')
            else:
                return redirect('movies:movie_list')
        else :
            form = MovieForm()
        context = {
            'form': form,

        }
        return render(request,'movies/form.html',context)
    else:
        return redirect('accounts:login')                 # accounts, url, view 작성해야됨




def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = request.user
    if user.is_authenticated:
        user_genre = int(user.genre)
    else:
        user_genre = 0
    context = {
        'movie': movie,
        'user_genre': user_genre,
    }

    return render(request, 'movies/movie_detail.html',context)


def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True

    context = {
        'count': movie.like_users.count(),
        'liked': liked,
    }
    return JsonResponse(context)

def movie_recommend(request):
    user = request.user
    
    genre = get_object_or_404(Genre, pk=int(user.genre))
    movies = genre.genre_movie.all()[:10]

    context = {
        'movies' : movies,

    }

    return render(request, 'movies/movie_recommend.html',context)


