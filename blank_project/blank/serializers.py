from rest_framework import serializers
from blank.models import Post, UserProfile
from django.contrib.auth.models import User


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


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = (
        'username',
        'user_id',
        #'photo',
        'i_am',
        'i_want',
        'i_need',
        'created',
        )
