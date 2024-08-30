from rest_framework import serializers

from .models import LogEntry


class LogEntrySerializer(serializers.ModelSerializer):
    """Serializer for route 'logs'."""

    class Meta:
        model = LogEntry
        fields = "__all__"
