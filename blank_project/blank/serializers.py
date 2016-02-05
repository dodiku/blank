from rest_framework import serializers
from blank.models import Post

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

    #PostSerializer class by using serializers.ModelSerializer
    #########################################################
    # pk = serializers.IntegerField(read_only=True)
    # i_am = serializers.CharField(required=True, max_length=50)
    # i_want = serializers.CharField(required=True, max_length=50)
    # i_need = serializers.CharField(required=True, max_length=50)
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Post` instance, given the validated data.
    #     """
    #     return Post.objects.create(**validated_data)
