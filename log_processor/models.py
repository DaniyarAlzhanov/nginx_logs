from django.db import models


class LogEntry(models.Model):
    remote_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField()
    method = models.CharField(max_length=10)
    uri = models.CharField(max_length=255)
    response_code = models.IntegerField()
    response_size = models.IntegerField()

    class Meta:
        verbose_name = "Nginx логи"
        verbose_name_plural = "Nginx логи"

    def __str__(self):
        return f"{self.remote_ip} - {self.method} {self.uri} {self.response_code}"
