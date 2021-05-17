from django.shortcuts import render

posts = [
    {
        'author': 'nikita',
        'title': 'post 1',
        'content': 'I love her',
        'date_posted': "May 18, 2020"
    },
    {
        'author': 'nelly',
        'title': 'post 2',
        'content': 'I love him',
        'date_posted': "May 18, 2020"
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
