from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Blog post model"""
    title = models.CharField(max_length=200, help_text="Title of the post")
    content = models.TextField(help_text="Content of the post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, help_text="Is the post published?")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title
