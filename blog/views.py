from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from .models import Article
from .serializers import ArticleSerializer,ArticleDetailSerializer,ArticleCreateSerilaizer


class ArticleListView(ListAPIView):

    permission_classes = (permissions.AllowAny,)
    queryset = Article.objects.all().order_by('-created_date','-created_time')
    serializer_class = ArticleSerializer
    
class ArticleDetailView(RetrieveAPIView):

    queryset = Article.objects.all()
    lookup_field = 'slug_field'
    serializer_class = ArticleDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        token = self.request.headers.get('Authorization','').split(' ')[1]
        user_obj = Token.objects.get(key=token).user
        context['user'] = user_obj
        return context

class ArticleCreateView(CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerilaizer

    def perform_create(self, serializer):
        token = self.request.headers.get('Authorization','').split(' ')[1]
        user_obj = Token.objects.get(key=token).user
        serializer.save(author=user_obj)
