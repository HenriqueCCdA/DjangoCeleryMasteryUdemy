from celery import shared_task

@shared_task
def task1():
    return "3"


@shared_task
def task2():
    return "4"
