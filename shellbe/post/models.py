from django.db import models
from django.utils.text import slugify

# Create your models here.

class AbstructBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True 
        
class PostsModel(AbstructBase):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts_pic')
    slug = models.SlugField(max_length=100, unique=True, blank=True)  
    content_type = models.CharField(
        max_length=100,
        choices=(
            ("Education", "Education"),
            ("Entertainment", "Entertainment"), 
            ("Sports", "Sports"),
            ("Food", "Food"),
            ("Gym", "Gym"),
        )
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)
        super(PostsModel, self).save(*args, **kwargs)
