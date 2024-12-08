from django.db import models
from django.contrib.auth.models import User
from users.models import Usercreate
from django.utils.text import slugify


class base(models.Model):
   
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Posts(base):
    user = models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    user_profile = models.ForeignKey(User,related_name="user_profile",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=100,choices=(('Education','Education'),('Entertainment','Entertainment'),('Food','Food'),('Sports','Sports')))
    slug = models.SlugField(max_length=100, blank=True,unique=True)
    media = models.CharField(max_length=100,choices=(('Images','Images'),('Videos','Videsos')))
    image = models.ImageField(upload_to='files',default='media/default_image.jpg') 
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
        

    
    
  
    
