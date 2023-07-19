from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Events)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["id", "event_title"]


@admin.register(models.EventResult)
class EventResultAdmin(admin.ModelAdmin):
    list_display = ["id"]
