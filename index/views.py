from django.views.generic import ListView

from article.models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
