from django.contrib import admin
from news.models import categories, articles

# Register your models here.

class articlesAdmin(admin.ModelAdmin):
    list_display=['title','slug','image','category','author','short_description','created_at', 'updated_at', 'status', 'is_trending']
    prepopulated_fields={'slug':('title',)}

admin.site.register(categories)
admin.site.register(articles, articlesAdmin)