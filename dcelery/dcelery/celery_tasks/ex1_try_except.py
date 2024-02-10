from dcelery.celery_config import app
from celery import Task
import logging


"""
from dcelery.celery_tasks.ex1_try_except import my_task
"""

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s',
)

class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection error occurred - Admin Notified')
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))

app.Task = CustomTask

@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection Error Occurred...")
    except ConnectionError:
        raise ConnectionError()
    except ValueError:
        # Handle value error
        logging.error("Value error occurrred...")
        # Perform specific error handling actions
        perform_specific_error_handling()
    except Exception:
        # Handle generic exceptions
        logging.error('An error occurred')
        # Notify administrators or perform fallback action
        notify_admin()
        perform_fallback_action()


def perform_specific_error_handling():
    # Logic to haandle a specific error scenario
    pass

def notify_admins():
    # Logic to send notifications to administrators
    pass
