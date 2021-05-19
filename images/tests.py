from images.views import my_gallery
from django.test import TestCase
from .models import Images,Location,Category


# Create your tests here.
class ImagesTestClass(TestCase):
    def setUp(self):
        self.test_category = Category(category=list('Travel'))
        self.test_category.save_category()

        self.location = Location(location="Home")
        self.location.save_location()

        self.image = Images(id=1,title="Slide Away",Category=self.test_category,location=self.location,)
        self.image.save_image()
    
    def test_save_image(self):
        self.image.save_image()
        image = Images.objects.all()
        self.assertTrue(len(image) > 0)


    def test_delete_image(self):
        self.image.delete_image()
        image=Images.objects.all()
        self.assertTrue(len(image)==0)

    def test_update_image(self):
        self.image.update_image()
        image=Images.objects.all()
        self.assertTrue(len(image)>1)

    

class LocationTestClass(TestCase):
    def setUp(self):
        self.Moringa = Location(location='Moringa')

    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Moringa.delete_location('Moringa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

    
class CategoryTestClass(TestCase):
    def setUp(self):
        self.Food = Category(category='Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.Food,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.Food.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Food.delete_category('Food')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)
