from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing blog posts.
    
    Provides CRUD operations for blog posts:
    - list: Get all posts
    - create: Create a new post
    - retrieve: Get a specific post
    - update: Update a post
    - partial_update: Partially update a post
    - destroy: Delete a post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Set the author to the current user when creating a post"""
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        """Ensure the author remains the same when updating"""
        serializer.save(author=self.request.user)
