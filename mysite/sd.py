from django_celery_beat.models import PeriodicTask, IntervalSchedule

schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
PeriodicTask.objects.create(
            interval=schedule,
            name='HI',
            task='mysite.tasks.test',
        )