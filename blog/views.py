from django.shortcuts import render

posts = [
    {
        'author': 'Lukasz Pasiak',
        'title': 'Post #1',
        'content': 'First post content',
        'date_posted': 'February 27, 2025'
    },
    {
        'author': 'Lukasz Psiapsiak',
        'title': 'Post #2',
        'content': 'Second post content',
        'date_posted': 'February 28, 2025'
    },
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})