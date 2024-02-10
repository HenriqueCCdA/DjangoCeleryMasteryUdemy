from multiprocessing import process
from dcelery.celery_config import app
from time import sleep
import sys


@app.task(queue="tasks", time_limit=10)
def long_running_task():
    sleep(6)
    return "Task completed successfully"


def process_task_result(self, result):
    if result is None:
        return "Task was evoked, skipping result processing"
    else:
        return f"Task result: {result}"


def execute_task_examples():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=40)
    except TimeoutError:
        print("Task time out")

    task = long_running_task.delay()
    task.revoke(terminate=True)

    sleep(3)
    sys.stdout.write(task.status)

    if task.status == 'REVOKED':
        process_task_result.delay(None)
    else:
        process_task_result.delay(task.result)
