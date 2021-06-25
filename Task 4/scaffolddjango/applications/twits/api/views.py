from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from applications.twits.models import Film, Review, Comment
from applications.twits.serializers import FilmSerializer, CommentSerializer, ReviewSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        film = get_object_or_404(Film, pk=self.kwargs.get('film_id'))
        queryset = Review.objects.filter(film=film)
        return queryset

    def perform_create(self, serializer):
        film = get_object_or_404(Film, pk=self.kwargs.get('film_id'))
        serializer.save(author=self.request.user, film=film)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        queryset = Comment.objects.filter(review=review)
        return queryset

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
