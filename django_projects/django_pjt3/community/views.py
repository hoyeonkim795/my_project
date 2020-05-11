from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Review, Comment
from .forms import ReviewForm
from .forms import CommentForm

# import json
# import urllib.request
# from django.shortcuts import render

# def search(request):

#     if request.method == 'GET':

#         config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())
#         client_id = config_secret_debug['NAVER']['CLIENT_ID']
#         client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']

#         q = request.GET.get('q')
#         encText = urllib.parse.quote("{}".format(q))
#         url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
#         movie_api_request = urllib.request.Request(url)
#         movie_api_request.add_header("X-Naver-Client-Id", client_id)
#         movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
#         response = urllib.request.urlopen(movie_api_request)
#         rescode = response.getcode()
#         if (rescode == 200):
#             response_body = response.read()
#             result = json.loads(response_body.decode('utf-8'))
#             items = result.get('items')
#             pprint(result)  # request를 예쁘게 출력해볼 수 있다.

#             context = {
#                 'items': items
#             }
#             return render(request, 'search/search.html', context=context)

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
def create(request):
    #POST
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES)

            # 유효성 검사
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('community:review_list')

            else:
                return redirect('community:review_list')

        #GET    (구 new)

        else :
            form = ReviewForm()
        context = {
            'form': form,

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

def update(request,pk):
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
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('community:review_list')