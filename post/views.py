from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from post.forms import PostCreationForm, PostUpdateForm, CommentForm
from post.models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(name=request.POST.get('name'),
                              email=request.POST.get('email'),
                              body=request.POST.get('body'),
                              post=self.get_object())
        new_comment.save()
        messages.success(request, f"Comment added successfully")
        return self.get(self, request, *args, **kwargs)


class PostCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'posts/post_create.html'
    success_message = 'Post was successfully created'

    """set author to be the current logged in user"""
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreationView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'posts/post_create.html'
    success_message = 'This post was updated successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False