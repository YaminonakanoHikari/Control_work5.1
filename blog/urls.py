from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comments/', CommentListCreateView.as_view(), name='post-comments'),
]