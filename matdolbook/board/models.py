from django.db import models
from matdolbook.users import models as user_models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True

class Content(TimeStampModel):
    #file = models.ImageField(null= True)
    text= models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete = models.CASCADE, related_name = 'contents')

    def __str__(self):
        lambda_text = lambda n : n[:25] + '...' if len(n)>25 else n
        return "{} - by {}".format(lambda_text(self.text) , self.creator.username)

    @property
    def comment_count(self):
        return self.comments.all().count()

    @property
    def like_count(self):
        return self.likes.all().count()

    class Meta:
        ordering = ['-created_at']

class Book(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    #content = models.ForeignKey(ContentsToBook , on_delete =models.CASCADE, related_name='contents')

    @property
    def interest_count(self):
        return self.interests.all().count()
    
    @property
    def content_count(self):
        return self.contentsAboutbook.all().count()

    def __str__(self):
        return "title - {} , author - {}".format(self.title, self.author)


class ContentToBook(TimeStampModel):
    text = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete = models.CASCADE, related_name = 'contentsTobook')
    bookinfo = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'contentsAboutbook')

    def __str__(self):
        lambda_text = lambda n : n[:25] + '...' if len(n)>25 else n
        return "{} - by {} BOOK: {}".format(lambda_text(self.text) , self.creator.username, self.bookinfo)

    @property
    def comment_count(self):
        return self.commentsBook.all().count()

    @property
    def like_count(self):
        return self.likesBook.all().count()

    class Meta:
        ordering = ['-created_at']

class Comment(TimeStampModel):
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete = models.CASCADE)
    content = models.ForeignKey(Content, on_delete= models.CASCADE, related_name= 'comments', null =True , blank= True)
    contentsToBook =models.ForeignKey(ContentToBook, on_delete= models.CASCADE, related_name = 'commentsBook', null = True, blank= True)
    #book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name ='comments')

    def __str__(self):
        return self.message

    @property
    def like_count(self):
        return self.likes.all().count()

    class Meta:
        ordering = ['-created_at']

#공감         
class LikeToContent(models.Model):
    creator = models.ForeignKey(user_models.User, on_delete = models.CASCADE, related_name= 'my_list')
    content = models.ForeignKey(Content, on_delete= models.CASCADE, related_name= 'likes', null =True, blank= True)
    contentsToBook =models.ForeignKey(ContentToBook, on_delete= models.CASCADE, related_name = 'likesBook', null= True, blank =True)

    def __str__(self):
        return "Creator - {} Content - {}".format(self.creator.username, )

class LikeToComment(models.Model):
    creator = models.ForeignKey(user_models.User, on_delete = models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE , related_name ='likes')

    def __str__(self):
        return "Creator - {} , Content - {}".format(self.creator.username, self.comment.message)

#담기
class AddCart(TimeStampModel):
    creator = models.ForeignKey(user_models.User, on_delete = models.CASCADE)
    content = models.ForeignKey(ContentToBook, on_delete = models.CASCADE ,related_name= 'addcarts')

    def __str__(self):
        return "Creator - {} , Content - {}".format(self.creator.username, self.content.text)

    class Meta:
        ordering = ['-created_at']

#관심책
class InterestToBook(models.Model):
    creator = models.ForeignKey(user_models.User ,on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE, related_name= 'interests')

    def __str__(self):
        return "{} interests {}".format(self.creator, self.book)