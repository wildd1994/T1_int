from django.urls import path, include
from rest_framework import routers
from applications.twits.api.views import FilmViewSet, ReviewViewSet, CommentViewSet


message_router = routers.DefaultRouter()
message_router.register(r'films', FilmViewSet)
message_router.register(r'films/(?P<film_id>.+)/review', ReviewViewSet, basename='reviews')
message_router.register(r'films/(?P<film_id>.+)/review/(?P<review_id>.+)/comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('', include(message_router.urls))
]
