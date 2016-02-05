from rest_framework import serializers
from blank.models import Post, UserProfile
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
        'user',
        'i_am',
        'i_want',
        'i_need',
        'created',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'username'
        )

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        picture = (
        'username'
        )
