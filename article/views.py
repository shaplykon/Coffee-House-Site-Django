from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content'}


class ArticleView(TemplateView):
    model = Post
    form = CommentForm
    template_name = 'article.html'


class CreatePageView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'


def PostDetail(self, pk):
    post = Post.objects.get(id=pk)
    comment = Comment.objects.filter(post_id=post.id)
    is_liked = False
    if post.likes.filter(id=self.user.pk).exists():
        is_liked = True
    if self.method == 'POST':
        form = CommentForm(self.POST)
        if form.is_valid():
            if self.user.is_authenticated:
                content = self.POST.get('content')
                comment = Comment.objects.create(post=post, user_id=self.user.pk, content=content)
                comment.save()
                return HttpResponseRedirect('/post/' + str(pk))
            else:
                return HttpResponseRedirect('http://localhost:8000/accounts/login/?next=/post/1/')
    else:
        form = CommentForm()

    return render(self, 'article.html', {'form': form, 'post': post, 'comment': comment, 'is_liked': is_liked,'current_user':User})


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.pk).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url(), {'is_liked': is_liked})


