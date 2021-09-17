from django.core import exceptions
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from .models import Article
from .serializers import ArticleSerializer,ArticleDetailSerializer


class ArticleListView(ListAPIView):

    permission_classes = (permissions.AllowAny,)
    queryset = Article.objects.all().order_by('-created_date')
    serializer_class = ArticleSerializer
    


class ArticleDetailView(RetrieveAPIView):

    queryset = Article.objects.all()
    lookup_field = 'slug_field'
    serializer_class = ArticleDetailSerializer

