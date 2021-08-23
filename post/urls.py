from django.urls import path
from .views import home, PostListView

app_name = 'post'
urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostListView.as_view(), name='post_list')
]