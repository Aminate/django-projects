from rest_framework.serializers import ModelSerializer
from .models import Post
from review.models import Comment
from review.serializers import CommentSerializer


# class CommentSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        #rep['likes'] = instance.likes.all().count()
        rep['comments'] = CommentSerializer(instance.comments.all(),many=True).data  #все коменты данного поста
        return rep