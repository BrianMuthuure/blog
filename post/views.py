from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from post.models import Post


def home(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        return context