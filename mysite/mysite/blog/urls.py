from django.urls.conf import include
from django.contrib import admin
from . import views
from django.urls import path, include
from .feeds import LatestPostFeed
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('feed/rss', LatestPostFeed(), name="post_feed"),
    path('tag/<slug:tag_slug>/', views.PostList.as_view(), name='post_tag')
]