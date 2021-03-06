from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# # ListCreateAPIView: read-write endpoint
# # @see https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
# class PostList(.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# # RetrieveUpdateDestoryAPIView: allow read, update, delete
# # @see https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer