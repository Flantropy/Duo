from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from api.serializers import PostSerializer
from blog.models import Post


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
