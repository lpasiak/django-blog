from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html by default
    context_object_name = 'posts' # object list by default
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
