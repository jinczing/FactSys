
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#@app.on_after_configure.connect
#def setup_periodic_tasks(sender, **kargs):
#    sender.add_periodic_task(10.0, hello.s('hello'), name='ten')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    
@app.task
def hello(arg):
    print(arg)
