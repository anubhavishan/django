from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

class Tweet(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    text= models.TextField(max_length=240)
    photo = CloudinaryField('photo', blank=True, null=True)
    # image = models.ImageField(upload_to='tweets/',blank=True,null=True)
    # photo= models.ImageField(upload_to='tweet_photos/',blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
