from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group as AuthGroup, Permission as AuthPermission

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='posts/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)