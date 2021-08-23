from django.urls.conf import include
from django.contrib import admin
from . import views
from django.urls import path, include
from .feeds import LatestPostFeed

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('feed/rss', LatestPostFeed(), name="post_feed"),
]