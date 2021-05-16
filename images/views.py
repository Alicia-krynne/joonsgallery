import images
from images.models import Images
from django.shortcuts import render
from django.http  import HttpResponse,Http404


# Create your views here.
def my_gallery(request):
    images = Images.my_gallery()
    return render(request, 'pics/home.html', {"images":images})

def show_images(request,images_title):
   
    try:
        images = Images.objects.get(id = images_title)
    except Images.DoesNotExist:
        raise Http404()
    return render(request,"all-news/my_gallery.html", {"images":images})
   
   
def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"gallery": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

   