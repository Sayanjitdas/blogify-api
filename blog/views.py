import json
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Article, Like, DisLike
from .serializers import ArticleSerializer, ArticleDetailSerializer, ArticleCreateSerilaizer


@api_view(['POST'])
def LikeView(request):
    try:
        user_model = get_user_model()
        data = json.loads(request.body)
        user_obj = user_model.objects.get(email=data.get('user'))
        article_obj = Article.objects.get(
            pk=int(data.get('article_id')))
        Like.objects.create(
            liked_article=article_obj,
            liked_by=user_obj
        )
    except Exception as e:
        print(e)
        return Response(status=400)
    return Response(status=201)


@api_view(['POST'])
def DisLikeView(request):
    pass


class ArticleListView(ListAPIView):

    permission_classes = (permissions.AllowAny,)
    queryset = Article.objects.all().order_by('-created_date', '-created_time')
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):

    queryset = Article.objects.all()
    lookup_field = 'slug_field'
    serializer_class = ArticleDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        token = self.request.headers.get('Authorization', '').split(' ')[1]
        user_obj = Token.objects.get(key=token).user
        context['user'] = user_obj
        return context


class ArticleCreateView(CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerilaizer

    def perform_create(self, serializer):
        token = self.request.headers.get('Authorization', '').split(' ')[1]
        user_obj = Token.objects.get(key=token).user
        serializer.save(author=user_obj)
