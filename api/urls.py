from django.urls import path

from api.views import PostList

urlpatterns = [
    path('posts/', PostList.as_view(), name='allposts'),
]
