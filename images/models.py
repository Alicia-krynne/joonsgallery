from django.db.models.deletion import  SET_DEFAULT, SET_NULL
from django.db.models.fields import CharField
import images
from django.db import models
# from location_field.models.plain import PlainLocationField
# from django.contrib.gis.geos import Point
from django import forms

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length =30)
  last_name = models.CharField(max_length =30)
  email = models.EmailField()

  def __str__(self):
        return self.first_name

  def save_user(self):
      self.save()


class Images(models.Model):
    image= models.ImageField(upload_to="media/")
    title=models.CharField(max_length=200)
    description= models.TextField(max_length=600)
    category = models.ForeignKey('Category',models.SET_NULL,null=True)
    location = models.ForeignKey('Location',models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    
   
    def __str__(self):
        return self.title

    @classmethod
    def my_gallery(cls):
        images = cls.objects
        return images

    @classmethod
    def show_images(cls):
        images=Images.objects.all()
        return images

    @classmethod
    def search_by_title(cls,search_term):
        images= cls.objects.filter(title__icontains=search_term)
        return images

class Category(models.Model): 
    category= models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Location(models.Model): 
    location= models.CharField(max_length=200)

    def __str__(self):
        return self.location



# class Address(forms.Form):
#   city = forms.CharField()
#   location = PlainLocationField(based_fields=['city'],
#   initial=Point(-49.1607606, -22.2876834))