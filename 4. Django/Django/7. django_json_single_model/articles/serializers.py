from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        #fields = '__all__'
        fields = ('id', 'title',)


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'