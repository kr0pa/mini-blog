from django.urls import path
from .views import BlogView, BlogCreateView

urlpatterns = [
    path('', BlogView.as_view(), name="home"),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
]