from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display_links = (
        'text',
    )

    search_fields = (
        'text',
    )

    list_display =(
        'text',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.ContentToBook)
class ContentToBookAdmin(admin.ModelAdmin):
    list_display_links = (
        'text',
    )

    search_fields = (
        'bookinfo',
    )

    list_display =(
        'text',
        'creator',
        'bookinfo',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =(
        'message',
        'creator',
        'content',
        'contentsToBook',
    )

@admin.register(models.LikeToComment)
class LikeTOCommentAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'comment',
    )

@admin.register(models.LikeToContent)
class LikeTOContentAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'content',
        'contentsToBook',
    )

@admin.register(models.AddCart)
class AddCartAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'content',
    )

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = (
        'title',
        'author',
        'interest_count',
    )

@admin.register(models.InterestToBook)
class InterestToBookAdmin(admin.ModelAdmin):

    list_display = (
        'creator',
        'book',
    )