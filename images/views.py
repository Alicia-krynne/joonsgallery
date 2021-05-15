from images.models import Images
from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def my_gallery(request):
    images = Images.my_gallery()
    return render(request, 'pics/home.html', {"images":images})