from django.db.models import fields
from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields = ('email','first_name','last_name','profile_pic')


class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    created_time = serializers.TimeField(format="%I:%M %p")
    class Meta:
        model = Article
        fields = ('title','slug_field','author','created_date','created_time')

class ArticleDetailSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ('title','slug_field','author','created_date','description')

class ArticleCreateSerilaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('title','description','slug_field')
        read_only_fields = ['slug_field',]
        