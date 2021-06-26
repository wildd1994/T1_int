from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Film(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    genre = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(max_length=5000)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.text
