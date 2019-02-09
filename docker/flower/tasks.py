from celery import Celery

app = Celery('tasks')


@app.task(bind=True)
def debug_task(self):
    # print("Request: {0!r}".format(self.request))
    # Calls repr() on the argument first
    print(f"Request: {self.request!r}")
