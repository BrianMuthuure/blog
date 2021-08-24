from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/%Y/%m/%d')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('date_created', )

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'