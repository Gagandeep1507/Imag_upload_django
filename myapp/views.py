from django.shortcuts import render, HttpResponse
from .forms import Imageform
from .models import Image
# Create your views here.


def Home(request):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = Imageform()
    else:
        form = Imageform()
        
    imgs = Image.objects.all()
    return render(request, 'myapp/home.html', {'imgs': imgs ,'form': form})