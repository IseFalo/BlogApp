from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# # Create your models here.
class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank= True, upload_to = 'profile_images/')
    def __str__(self) :
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    post_image = models.ImageField(null=True, blank=True, upload_to = 'images/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering = ('-updated',)

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('-create_date',)


    def __str__(self):
        return '%s-%s' % (self.post.title, self.comment_author)

    
