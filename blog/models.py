from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import constraints
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

class Like(models.Model):

    liked_article = models.ForeignKey(Article,related_name='article_liked',on_delete=models.CASCADE)
    liked_by = models.ForeignKey(USER,related_name='liked_by_user',on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['liked_article','liked_by'],name='like_once')
        ]
    

    def __str__(self):
        return f"{self.liked_article.slug_field} liked by {self.liked_by}" 

class DisLike(models.Model):

    disliked_article = models.ForeignKey(Article,related_name='article_disliked',on_delete=models.CASCADE)
    disliked_by = models.ForeignKey(USER,related_name='disliked_by_user',on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['disliked_article','disliked_by'],name='dislike_once')
        ]
    
    def __str__(self):
        return f"{self.disliked_article.article_liked} disliked by {self.disliked_by}" 