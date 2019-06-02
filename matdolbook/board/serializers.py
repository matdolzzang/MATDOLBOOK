from rest_framework import serializers
from . import models
from matdolbook.users import models as user_models
import re

class BoardUserSerilizer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'profile_image',
            'username',
        )

class CommetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None,read_only=True)
    creator= BoardUserSerilizer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'creator',
            'message',
            'created_at',
            'like_count'
        )

class ContentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    creator = BoardUserSerilizer()
    comments = CommetSerializer(many = True)
    class Meta:
        model = models.Content
        fields = (
            'id',
            'creator',
            'text',
            'comments', #당장은 보기 편하게.
            'comment_count',
            'like_count',
            'created_at',
        )

class ContentDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    creator = BoardUserSerilizer()
    comments = CommetSerializer(many = True)
    class Meta:
        model = models.Content
        fields = (
            'id',
            'creator',
            'text',
            'comments',
            'like_count',
            'created_at',
        )

class InputContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = (
            'text',
        )

class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = (
            'title',
            'author',
        )

class ContentToBookSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    creator = BoardUserSerilizer()
    bookinfo = BookInfoSerializer()
    commentsBook = CommetSerializer(many = True)
    class Meta:
        model = models.ContentToBook
        fields = (
            'id',
            'creator',
            'text',
            'bookinfo',
            'commentsBook', #당장은 보기편하게
            'comment_count',
            'like_count',
            'created_at',
        )

class ContentToBookDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)
    creator = BoardUserSerilizer()
    bookinfo = BookInfoSerializer()
    commentsBook = CommetSerializer(many = True)
    class Meta:
        model = models.ContentToBook
        fields = (
            'id',
            'creator',
            'text',
            'bookinfo',
            'commentsBook',
            'like_count',
            'created_at',
        )

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = (
            'title',
            'author',
            'interest_count',
            'content_count',
        )

class BookDetailSerializer(serializers.ModelSerializer):

    contentsAboutbook = ContentToBookSerializer(many= True)
    class Meta:
        model = models.Book
        fields = (
            'title',
            'author',
            'contentsAboutbook',
            'interest_count',
            'content_count',
        )
        
class InputContentToBookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ContentToBook
        fields = (
            'text',
            'bookinfo',
        )
