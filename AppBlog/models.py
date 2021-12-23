from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postauthor')
    blogtittle = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is on Your mind?")
    blog_image = models.ImageField(upload_to='blogimage', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blogtittle


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="like_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")
