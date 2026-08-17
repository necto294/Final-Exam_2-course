from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model"""
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author',
            'author_name',
            'created_at',
            'updated_at',
            'is_published',
        ]
        read_only_fields = ['created_at', 'updated_at']
