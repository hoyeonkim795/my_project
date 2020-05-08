from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Community
from .forms import CommunityForm

# Create your views here.
def photolist(request):
    photolists = Community.objects.all()
    context ={
        'photolists':photolists
    }
    return render(request, 'community/photolist.html',context)

def create(request):
    #POST
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('community:photolist')

        else:
            return redirect('community:photolist')


    else :
        form = CommunityForm()
    context = {
        'form': form,

    }
    return render(request,'community/form.html',context)

