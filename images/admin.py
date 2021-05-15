from django.contrib import admin
from .models import  User,Images,Category
# Register your models here.


#class ArticleAdmin(admin.ModelAdmin):
    #filter_horizontal =('tags',)


admin.site.register(User)
admin.site.register(Images)
admin.site.register(Category)

#admin.site.register (Address)
