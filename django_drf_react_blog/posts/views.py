from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


# ListCreateAPIView: read-write endpoint
# @see https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestoryAPIView: allow read, update, delete
# @see https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer