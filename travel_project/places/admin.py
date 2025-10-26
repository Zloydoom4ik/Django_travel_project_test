from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['preview']
    
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px;" />',
                obj.image.url
            )
        return "Нет изображения"
    
    preview.short_description = 'Превью'

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lat', 'lng')
    inlines = (
        ImageInline,
    )
