from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from accounts.models import Account


class Post(models.Model):
    title = models.CharField(max_length=200, default='')
    author = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        default='',
    )
    body = models.TextField(default='')
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(Account, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(str(self.user.get_username()))
