from rest_framework import serializers

from posts.models import Post
from users.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)  # Nested serializer

    # Providing a serializer for profile is necessary for serving profile data

    class Meta:
        model = Post
        fields = [
            "pk",
            "profile",
            "title",
            "body",
            "image",
            "publication_date",
            "likes",
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "category",
            "body",
            "image"
        ]
