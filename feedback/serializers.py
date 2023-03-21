from rest_framework import serializers
from feedback.models import Like, Comment, Rating, Favorite

class likeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__' 

# class CommentSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.email')

#     class Meta:
#         model = Comment
#         fields = '__all__'

class RatingSerializers(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    
    class Meta:
        model = Rating
        fields = ('rating',)

class FavoriteSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Favorite
        fields = '__all__'
