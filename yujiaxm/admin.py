from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
# Register your models here.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'username','name','img','place','distance','assess'
    ]
    search_fields = [
        'username'
    ]
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name','title','img','people'
    ]
    search_fields = [
        'name'
    ]
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = [
        'name','img'
    ]
    search_fields = [
        'name'
    ]
@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = [
        'name','img'
    ]
    search_fields = [
        'name'
    ]
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = [
        'name','t'
    ]
    search_fields = [
        'name'
    ]






admin.AdminSite.site_header = "瑜+后台界面"
admin.AdminSite.index_title = "瑜+后台"