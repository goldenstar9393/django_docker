import json

from marshmallow import ValidationError
from django.views.generic import View

from rest_framework import generics
from techtest.articles.models import Article
from techtest.articles.schemas import ArticleSchema
from techtest.utils import json_response


class ArticlesListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSchema


class ArticleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSchema