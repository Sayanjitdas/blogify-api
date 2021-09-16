from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

USER = get_user_model()

class Article(models.Model):

    title = models.CharField(max_length=250)
    slug_field = models.SlugField(unique=True)
    author = models.ForeignKey(USER,related_name='author',on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True,blank=True,null=True)
    created_time = models.TimeField(auto_now_add=True,blank=True,null=True)
    description = models.TextField()
    
    def save(self, *args,**kwargs) -> None:
        self.slug_field = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title[:20]
