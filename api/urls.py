from django.urls import path

from api.views import PostList, PostRetrieve

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', PostRetrieve.as_view(), name='post')
]
