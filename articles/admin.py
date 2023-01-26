from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Articles

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'get_img')
    list_display_links = ('title',)
    fields = ('author', 'title', 'body', 'image',)


    def get_img(self, details):
        if details.image:
            return mark_safe(f'<img src="{ details.image.url }" width="80px"')
        else:
            return 'Нет картинки'

    get_img.short_description = 'Миниатюра'

admin.site.register(Articles, ArticlesAdmin)