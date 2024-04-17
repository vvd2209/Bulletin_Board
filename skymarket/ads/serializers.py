from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'ad', 'created_at',)


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'price', 'description', 'created_at',)
