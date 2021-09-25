from typing import List
from django.contrib import admin
from .models import Article,Like,DisLike


class LikeAdmin(admin.StackedInline):
    model = Like
    extra = 0
    fk_name = 'liked_article'
    verbose_name = ' '
    readonly_fields = ['liked_by']
    
    def has_add_permission(self,request,obj):
        return False

    def has_delete_permission(self,request,obj):
        return False

class DisLikeAdmin(admin.StackedInline):
    model = DisLike
    extra = 0
    fk_name = 'disliked_article'
    verbose_name = ' '
    verbose_name_plural = 'DISLIKES'
    readonly_fields = ['disliked_by']
    
    def has_add_permission(self,request,obj):
        return False

    def has_delete_permission(self,request,obj):
        return False
    


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title','author','created_date']
    inlines = [
        LikeAdmin,
        DisLikeAdmin
    ]