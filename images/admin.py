from django.contrib import admin
from .models import  Category, Location,Images
# Register your models here.


#class ArticleAdmin(admin.ModelAdmin):
    #filter_horizontal =('tags',)


admin.site.register(Images)
admin.site.register(Location)
admin.site.register(Category)


#admin.site.register (Address)
