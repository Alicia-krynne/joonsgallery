from images.models import Images
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def my_gallery(request):
    images = Images.my_gallery()
    return render(request, 'all-images/my_gallery.html', {"images":images})