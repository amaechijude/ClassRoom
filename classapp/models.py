from django.db import models
from django.contrib.auth.models import User

# Third party
from taggit.managers import TaggableManager
from django_resized import ResizedImageField

# Create your models here.

class PostModel(models.Model):
    pid = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, default='title', blank=True)
    img = ResizedImageField(quality=70, upload_to='media/posts', blank=True, null=True)
    #slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    
    # class Meta:
    #     ordered_by = 'created_at'
    def __str__(self):
        return f"{self.title}"
    
    
class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, default='title')
    img = ResizedImageField(quality=70, upload_to='media/comments', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     ordered_by = 'created_at'
    def __str__(self):
        return f"{self.title}"
    
