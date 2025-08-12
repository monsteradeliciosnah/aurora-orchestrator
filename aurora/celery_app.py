import os

from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
celery = Celery("aurora", broker=REDIS_URL, backend=REDIS_URL)


@celery.task(name="aurora.add")
def add(x: int, y: int) -> int:
    return x + y
