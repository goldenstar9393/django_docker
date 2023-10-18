"""techtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from techtest.articles.views import ArticleView, ArticlesListView
from techtest.regions.views import RegionView, RegionsListView
from techtest.authors.views import AuthorList, AuthorDetail
schema_view = get_schema_view(
    openapi.Info(
        title="TechTask",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="pradlashodoski626@outlook.com"),
        license=openapi.License(name="This is license for openai"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/', include('techtest.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("articles/", ArticlesListView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticleView.as_view(), name="article"),
    path("regions/", RegionsListView.as_view(), name="regions-list"),
    path("regions/<int:pk>/", RegionView.as_view(), name="region"),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]
