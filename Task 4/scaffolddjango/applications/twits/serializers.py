from rest_framework import serializers
from applications.twits.models import Film, Comment, Review

# class CustomerSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()
#
#     @staticmethod
#     def get_full_name(obj):
#         return obj.first_name + " " + obj.last_name
#
#     class Meta:
#         model = Customer
#         exclude = ()
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     customer = CustomerSerializer(many=False, read_only=False)
#
#     class Meta:
#         model = Order
#         exclude = ()
#
#
# class MessageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Message
#         exclude = ()


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
