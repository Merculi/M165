from datetime import datetime

import psutil


class Power:
    def __init__(self, cpu=None, ram_total=None, ram_used=None, timestamp=None, _id=None):
        if _id is not None:
            self._id = _id

        if cpu is None:
            cpu = psutil.cpu_percent(interval=1)

        memory = psutil.virtual_memory()

        if ram_total is None:
            ram_total = memory.total

        if ram_used is None:
            ram_used = memory.used

        if timestamp is None:
            timestamp = datetime.now()

        self.cpu = cpu
        self.ram_total = ram_total
        self.ram_used = ram_used
        self.timestamp = timestamp
