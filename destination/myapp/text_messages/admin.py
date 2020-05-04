from django.contrib import admin

from .models import TextMessage


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    list_display = (
        'message',
    )
