from django.contrib import admin
from .models import Cars,Comment

@admin.register(Cars)

class CarAdmin(admin.ModelAdmin):
    list_display=["marka","author"]
    list_display_links=["marka","author"]
    list_filter=["added_date"]
    search_fields=["marka"]
    class Meta:
        model=Cars

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display=["author"]
    list_display_links=["author"]
    list_filter=["added_date"]
    search_fields=["author"]
    class Meta:
        model=Comment

# Register your models here.
