from rest_framework import serializers
from applications.twits.models import Film, Comment, Review


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Film


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    film = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    review = ReviewSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
