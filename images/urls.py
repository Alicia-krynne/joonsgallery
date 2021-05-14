from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.my_gallery,name='myGallery'),
    #path('gallery/<str:past_date>/',views.past_days_news,name='pastNews'),  #change  this Url
    #path('search/', views.search_results, name='search_results'),
    #path('gallery/<int:article_id>',views.gallery,name ='gallery')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)