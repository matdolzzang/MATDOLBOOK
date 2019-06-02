from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
#from nomadgram.notification import views as notification_views
from matdolbook.users import models as user_models
#from nomadgram.users import serializers as user_serializers

def FoundContent(content_id):
    try:
        found_content = models.Content.objects.get(id = content_id)
        return found_content
    except models.Content.DoesNotExist:
        return Response(status = HTTP_404_NOT_FOUND)

def FoundContentBook(content_id):
    try:
        found_content = models.ContentToBook.objects.get(id = content_id)
        return found_content
    except models.ContentToBook.DoesNotExist:
        return Response(status = HTTP_404_NOT_FOUND)


class Content(APIView):

    def get(self, request ,format = None):
        contents = models.Content.objects.all()
        serializer = serializers.ContentSerializer(contents, many =True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)

    def post(self, request, format =None):
        user = request.user
        serializer= serializers.InputContentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(creator = user)
            return Response(data = serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ContentDetail(APIView):

    def get(self, request, content_id, format = None):
        content = FoundContent(content_id)
        serializer = serializers.ContentDetailSerializer(content)
        return Response(data = serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, content_id, format= None):
        user = request.user
        try:
            old_content = models.Content.objects.get(creator = user, id = content_id)
            old_content.delete()
            return Response(status=  status.HTTP_204_NO_CONTENT)
        except models.Content.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, content_id , format =None):
        user = request.user
        try:
            revise_content = models.Content.objects.get(creator = user, id = content_id)
        except models.Content.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        serializer = serializers.InputContentSerializer(
            revise_content,
            data = request.data,
            partial = True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class ContentBest(APIView):

    def get(self, request ,format = None):
        contents = models.Content.objects.all()
        serializer = serializers.ContentSerializer(contents, many =True)
        serializer = serializer.data
        serializer.sort(key=lambda x:x['like_count'], reverse =True)
        return Response(data = serializer , status = status.HTTP_200_OK)

class CommentOnContent(APIView):

    def post(self, request, content_id, format=None):
        user =request.user
        serializer = serializers.CommetSerializer(data = request.data)
        """try:
            found_content= models.Content.objects.get(id = content_id)
        except models.Content.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        """
        found_content = FoundContent(content_id)
        if serializer.is_valid():
            serializer.save(creator = user, content = found_content)
            return Response(data =serializer.data ,status = status.HTTP_201_CREATED)
        else:
            return Response(data =serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CommentChange(APIView):
    
    def delete(self, request, content_id, comment_id, format = None):
        user = request.user
        try:
            old_comment = models.Comment.objects.get(
            creator = user,
            id = comment_id
            )
            old_comment.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

    def put(self, request, content_id, comment_id, format = None):
        user = request.user
        try:
            revise_comment = models.Comment.objects.get(
                creator= user,
                id = comment_id
            )
        except models.Comment.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.CommetSerializer(revise_comment, data= request.data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data =serializer.data , status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(data =serializer.data , status = status.HTTP_400_BAD_REQUEST)

class LikeContent(APIView):

    def post(self, request , content_id, format =None):
        user =request.user
        found_content = FoundContent(content_id)
        try:
            old_like = models.LikeToContent.objects.get(creator = user, content =found_content)
            return Response(status = status.HTTP_304_NOT_MODIFIED)
        except models.LikeToContent.DoesNotExist:
            new_like = models.LikeToContent.objects.create(
                creator = user,
                content = found_content,
            )
            return Response(status = status.HTTP_201_CREATED)

class UnlikeContent(APIView):

    def delete(self, request, content_id, format = None):
        user = request.user
        found_content = FoundContent(content_id)
        try:
            old_like = models.LikeToContent.objects.get(creator = user, content = found_content)
            old_like.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except models.LikeToContent.DoesNotExist:
            return Response(status = status.HTTP_304_NOT_MODIFIED)

class ContentBook(APIView):

    def get(self, request ,format = None):
        contents = models.ContentToBook.objects.all()
        serializer = serializers.ContentToBookSerializer(contents, many =True)
        return Response(data = serializer.data , status = status.HTTP_200_OK)

    def post(self, request, format =None):
        user = request.user
        serializer= serializers.InputContentToBookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(creator = user)
            return Response(data = serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ContentBookDetail(APIView):

    def get(self, request, contentbook_id, format= None):
        content = FoundContentBook(contentbook_id)
        serializer = serializers.ContentToBookDetailSerializer(content)
        return Response(data = serializer.data, status = status.HTTP_200_OK)

