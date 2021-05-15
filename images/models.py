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
    image= models.ImageField(upload_to="gallery/")
    title=models.CharField(max_length=200)
    description= models.TextField(max_length=600)
    Category = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    
   

    def __str__(self):
        return self.title

    @classmethod
    def my_gallery(cls):
        images = cls.objects
        return images

class Category(models.Model):
    Category = models.ManyToManyField(Images)

    def __str__(self):
        return self.name 


# class Address(forms.Form):
#   city = forms.CharField()
#   location = PlainLocationField(based_fields=['city'],
#   initial=Point(-49.1607606, -22.2876834))