from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from api.serializers import PostSerializer
from blog.models import Post


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class PostRetrieve(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
