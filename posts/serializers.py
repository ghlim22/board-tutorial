from rest_framework import serializers

from posts.models import Post, Comment
from users.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "pk",
            "profile",
            "post",
            "text"
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "post",
            "text"
        ]


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)  # Nested serializer
    comments = CommentSerializer(many=True, read_only=True)

    # Providing a serializer for profile is necessary for serving profile data

    class Meta:
        model = Post
        fields = '__all__'
        # fields = [
        #     "pk",
        #     "profile",
        #     "title",
        #     "body",
        #     "image",
        #     "publication_date",
        #     "likes",
        #     "comments"
        # ]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "category",
            "body",
            "image"
        ]
