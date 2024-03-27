from django.contrib import admin

# Register your models here.

from .models import Article

# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["title","created_date"]
    class Meta:
        model = Article