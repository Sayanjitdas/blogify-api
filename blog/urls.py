from django.urls import path
from .views import ArticleListView,ArticleDetailView

urlpatterns = [
    path('',ArticleListView.as_view(),name="view-articles"),
    path('<str:slug_field>/',ArticleDetailView.as_view(),name="view-detail-articles")
]