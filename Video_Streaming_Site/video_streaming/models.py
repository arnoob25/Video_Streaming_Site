import urllib.parse
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

class Video(models.Model):
    author = models.ForeignKey(get_user_model(), blank=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    source = models.URLField(max_length=500)
    thumbnail = models.URLField(max_length=500, blank=True)
    category_choices = [
        ('1', 'Machine Learning'),
        ('2', 'Economics'),
        ('3', 'Geopolitics'),
        ('4', 'Game Development'),
        ('5', 'Startups'),
    ]
    category = models.CharField(max_length=50, choices=category_choices, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def get_thumbnail_url(self):
        parsed_url = urllib.parse.urlparse(self.source)
        video_id = parsed_url.path.split('/')[-1]
        
        return f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        
    # generating the slug and thumbnail url
    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is newly created
            self.thumbnail = self.get_thumbnail_url()
            self.slug = slugify(self.title)  # Generate slug from title
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)