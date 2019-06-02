from . import views 
from django.urls import include, path

app_name = "board"
urlpatterns = [
    path("", view= views.Content.as_view()),
    path("<int:content_id>/", view = views.ContentDetail.as_view()),
    path("best/", view = views.ContentBest.as_view()),
    path("<int:content_id>/comments/", view = views.CommentOnContent.as_view()),
    path("<int:content_id>/likes/", view = views.LikeContent.as_view()),
    path("<int:content_id>/unlikes/", view = views.UnlikeContent.as_view()),
    path("<int:content_id>/comments/<int:comment_id>/", view = views.CommentChange.as_view()),
    path("book/", view = views.ContentBook.as_view()),
    path("book/<int:contentbook_id>/", view=  views.ContentBookDetail.as_view())
]