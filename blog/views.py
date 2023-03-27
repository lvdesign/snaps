from django.shortcuts import render, redirect
from .models import Post
from .forms import ImageForm

from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'post_list.html', ctx)


def loadImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list.html')
    else:
            form= ImageForm()
            ctx = {'form':form}
    return render(request, 'load.html', ctx)