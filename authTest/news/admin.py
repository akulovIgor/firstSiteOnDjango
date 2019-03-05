from django.contrib import admin
from news.models import Articles, Comments


class ArticlesInLine(admin.StackedInline):
    model = Comments
    extra = 2


class ArticlesAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'date']
    inlines = [ArticlesInLine]


admin.site.register(Articles, ArticlesAdmin)
# Register your models here.
