from django.contrib import admin

from .models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "remote_ip",
        "timestamp",
        "method",
        "uri",
        "response_code",
        "response_size",
    )
    search_fields = (
        "remote_ip",
        "timestamp",
        "method",
        "uri",
    )
    list_filter = (
        "timestamp",
        "method",
        "uri",
        "response_code",
    )
