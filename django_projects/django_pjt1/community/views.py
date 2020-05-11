from django.shortcuts import render,redirect
from .models import Review
# Create your views here. project
def review_list(request):
    reviews= Review.objects.all()
    context = {
        'reviews':reviews,


    }
    return render(request, 'review_list.html',context)

def new_review(request): #데이터를 작성할 페이지  #new
    return render(request, 'new_review.html')

def create_review(request): #데이터를 DB에 저장하는 로직  #create
    title = request.GET.get('title')
    content = request.GET.get('content')
    rank = request.GET.get('rank')
    #create
    article = Review(title=title, content=content, rank=rank)
    article.save()
    return redirect(f'/review_detail/{review.pk}/')

def review_detail(request,review_pk):

    review= Review.objects.get(id=review_pk)
    context = {

        'review':review,
    }
    return render(request, 'review_detail.html',context)