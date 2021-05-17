from images.views import my_gallery
from django.test import TestCase
from .models import User,Images


# Create your tests here.
class UserTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.macrine= User(first_name = 'Macrine', last_name ='Alice', email ='alicakrynne@outlook.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.macrine,User))

    # Testing Save Method
    def test_save_method(self):
        self.macrine.save_user()
        user = User.objects.all()
        self.assertTrue(len(user) > 0)
    
class ImagesTestClass(TestCase):

    def setUp(self):
        # Creating a new user and saving it
        self.macrine= User(first_name = 'Macrine', last_name ='Alice', email ='alicakrynne@outlook.com')
        self.macrine.save_user()

        # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

        self.new_image= Images(title = 'Test Images',post = 'This is a random test Post',editor = self.macrine)
        self.new_image.save()

        self.new_image.category.add(self.new_tag)

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Images.objects.all().delete()

def test_save_image(self):
    self.image.save_image()
    image = Images.objects.all()
    self.assertTrue(len(image) > 0)




    

