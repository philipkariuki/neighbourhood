from django.test import TestCase
from .models import Post, UserProfile

class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.posty= Post(title = 'zproject Mpya', description ='Hii ni description ya test project', postimage='postpics/project.png')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.posty,Post))

    # Testing Save Method
    def test_save_method(self):
        self.posty.save_project()
        
            
    # Testing new project
    def test_new_post(self):
        self.new_post= Post(title = 'Test Project',description = 'This is a random test post description', postimage='articles/project.png')
        self.new_post.save()
        
    def tearDown(self):
        Project.objects.all().delete()
  

class UserProfileTestClass(TestCase):
         
    def setUp(self):
        self.pablo = Profile(name='pablo', bio='hii ni bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.pablo, UserProfile))
        
    
    def tearDown(self):
        UserProfile.objects.all().delete()
        
    



