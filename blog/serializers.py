from django.db.models import fields
from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

USER = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=get_user_model()
        fields = ('email','first_name','last_name')


class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ('title','slug_field','author','created_date')

class ArticleDetailSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ('title','slug_field','author','created_date','description')