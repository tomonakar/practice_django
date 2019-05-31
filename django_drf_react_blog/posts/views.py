from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer


# ListCreateAPIView: read-write endpoint
# @see https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestoryAPIView: allow read, update, delete
# @see https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer