from django.shortcuts import render

posts = [
    {
        'author': 'nikita',
        'title': 'post 1',
        'content': 'content of post 1'
    },
    {
        'author': 'nelly',
        'title': 'post 2',
        'content': 'hello world'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Welcome'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
