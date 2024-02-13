from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group as AuthGroup, Permission as AuthPermission
from django.urls import reverse
from ckeditor.fields import RichTextField

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    profile_pic = models.ImageField(null=True, upload_to='profile/')
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    full_text = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/', default='../../media/posts/default.webp')

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.post_id)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s - %s' % (self.user.first_name, self.user.last_name, self.post.title)