from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



class Thahood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def save_thahood(self):
        self.save()

    @classmethod
    def delete_thahood(self):
        self.delete()
    @classmethod
    def get_thahood(cls):
    	hoodz = cls.objects.all()
    	return hoodz



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length =260)    
    pub_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(default=0, max_length =14)
    pic = models.ImageField(upload_to = 'profilepics2/', blank=True )
    neighbourhood = models.ForeignKey(Thahood)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


        
class Post(models.Model):
    title = models.CharField(max_length =60)
    description = HTMLField()
    poster = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)
    postimage = models.ImageField(upload_to = 'postpics/', blank=True )
    postedby = models.ForeignKey(UserProfile)
    hood = models.ForeignKey(Thahood)


    def __str__(self):
        return self.title

    class Meta:
        ordering =['pub_date']
    
    
    @classmethod
    def get_postss(cls):
        projos = cls.objects.all()
        return projos


    @classmethod
    def search_by_title(cls,search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts


    def delete_post(self):
        self.delete()       

    def save_post(self):
        self.save()



class Business(models.Model):    
    name = models.CharField(max_length=70)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Thahood)
    email = models.EmailField()
    pub_date = models.DateTimeField(default=timezone.now)
    biz_image = models.ImageField(default = 'default.jpg',upload_to='bizpics/')
    
    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        bizna = cls.objects.filter(name__icontains=search_term) | cls.objects.filter(category__icontains=search_term)
        return bizna
    
    @classmethod
    def update_business(id):
        Business.objects.filter(id=id).update()