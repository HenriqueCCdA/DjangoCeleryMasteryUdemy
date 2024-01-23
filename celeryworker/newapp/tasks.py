from celery import shared_task

@shared_task
def task1():
    return "1"


@shared_task
def task2():
    return "1"
