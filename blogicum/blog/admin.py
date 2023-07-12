from django.contrib import admin

from .models import Location, Category, Post, Comment


class BlogAdmin(admin.ModelAdmin):
    """Интерфейс админ-панели."""

    list_editable = (
        "is_published",
    )


class CommentAdmin(admin.TabularInline):
    """Интерфейс комментариев."""
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(BlogAdmin):
    """Интерфейс постов."""
    list_display = (
        "title",
        "is_published",
        "pub_date",
        "author",
        "comment_count",
        "get_post_img",
    )
    search_fields = (
        "title",
        "text",
    )
    list_filter = (
        "is_published",
        "category",
        "location",
        "author",
    )
    fields = (
        "is_published",
        "title",
        "text",
        "pub_date",
        "author",
        "location",
        "category",
        "get_post_img",
        "image",
    )

    @admin.display(description="Изображение")
    def get_post_img(self, obj):
        if obj.image:
            return (f"<img src='{obj.image.url}' width=50")

    @admin.display(description="Комментарии")
    def comment_count(self, obj):
        return obj.comments.count()


@admin.register(Category)
class CategoryAdmin(BlogAdmin):
    """Интерфейс категорий."""

    list_display = (
        "title",
        "is_published",
        "created_at",
        "slug",
    )


@admin.register(Location)
class LocationAdmin(BlogAdmin):
    """Интерфейс местоположения."""

    list_display = (
        "name",
        "is_published",
        "created_at",
    )
