from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail_preview', 'category']
    list_filter = ['category']
    search_fields = ['name']

    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="{obj.thumbnail.url}" style="width:200px; height:auto;">')


class WorkImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail_preview']

    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="{obj.img.thumbnail.url}" style="width:200px; height:auto;">')


class CraftAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail_preview']
    search_fields = ['name']

    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="{obj.thumbnail.url}" style="width:200px; height:auto;">')


class CraftImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail_preview']

    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="{obj.img.thumbnail.url}" style="width:200px; height:auto;">')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'business', 'tel', 'fax', 'email', 'address']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'send_by', 'tel', 'content', 'created_at']
    search_fields = ['name', 'created_at']


admin.site.register(Work, WorkAdmin)
admin.site.register(WorkImage, WorkImageAdmin)
admin.site.register(Craft, CraftAdmin)
admin.site.register(CraftImage, CraftImageAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
