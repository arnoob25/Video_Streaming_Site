from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    source = models.URLField(max_length=500)
    category_choices = [
        ('1', 'Machine Learning'),
        ('2', 'Economics'),
        ('3', 'Geopolitics'),
        ('4', 'Game Development'),
        ('5', 'Startups'),
    ]
    category = models.CharField(max_length=50, choices=category_choices, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    # generating the slug
    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is newly created
            self.slug = slugify(self.title)  # Generate slug from title
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)