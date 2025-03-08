from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html by default
    context_object_name = 'posts' # object list by default
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    # Override the form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
