import json
from datetime import datetime as dt

from django.core.management.base import BaseCommand

from log_processor.models import LogEntry


class Command(BaseCommand):
    help = "Import Nginx logs from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        with open(file_path, "r") as file:
            for line in file:
                data = json.loads(line)
                LogEntry.objects.create(
                    remote_ip=data["remote_ip"],
                    timestamp=dt.strptime(data["time"], "%d/%b/%Y:%H:%M:%S %z"),
                    method=data["request"].split()[0],
                    uri=data["request"].split()[1],
                    response_code=data["response"],
                    response_size=data["bytes"],
                )

        self.stdout.write(self.style.SUCCESS("Successfully imported logs"))
