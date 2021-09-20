from django.urls import path
from .views import ArticleListView,ArticleDetailView,ArticleCreateView

urlpatterns = [
    path('',ArticleListView.as_view(),name="view-articles"),
    path('create-post/',ArticleCreateView.as_view(),name="create-post"),
    path('<str:slug_field>/',ArticleDetailView.as_view(),name="view-detail-articles"),

]