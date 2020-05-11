from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.all()
    context ={
        'reviews':reviews
    }
    return render(request, 'community/review_list.html',context)

def create(request):
    #POST
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # 유효성 검사
        if form.is_valid():
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


def review_detail(request,pk):
    review= get_object_or_404(Review, pk=pk)
    context = {

        'review': review,
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