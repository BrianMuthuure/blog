from django.urls import path
from .views import PostListView, PostDetailView, PostCreationView, PostUpdateView, PostDeleteView

app_name = 'post'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create-post/', PostCreationView.as_view(), name='create_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]