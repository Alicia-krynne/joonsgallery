from django.db import models

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
    category = models.ManyToManyField() 
    location= models.ForeignKey()
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    
   
    
    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length =100)

    def __str__(self):
        return self.name