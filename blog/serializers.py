from rest_framework import serializers
from .models import Article,Like,DisLike
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields = ('email','first_name','last_name','profile_pic')


class ArticleSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    author = AuthorSerializer()
    created_time = serializers.TimeField(format="%I:%M %p")
    class Meta:
        model = Article
        fields = ('title','slug_field','author','created_date','created_time','likes','dislikes')

    def get_likes(self,instance):
        return Like.objects.filter(liked_article=instance).count()

    def get_dislikes(self,instance):
        return DisLike.objects.filter(disliked_article=instance).count()
        

class ArticleDetailSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    author = AuthorSerializer()
    created_time = serializers.TimeField(format="%I:%M %p")
    class Meta:
        model = Article
        fields = ('title','slug_field','author','created_date','created_time','description','likes','dislikes')

    def get_likes(self,instance):
        return Like.objects.filter(liked_article=instance).count()

    def get_dislikes(self,instance):
        return DisLike.objects.filter(disliked_article=instance).count()


class ArticleCreateSerilaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('title','description','slug_field')
        read_only_fields = ['slug_field',]
        