from django_cron import CronJobBase, Schedule
from .models import Subscriptions
from datetime import datetime,timedelta

class CheckSubscriptions(CronJobBase):
    RUN_EVERY_MINS = 5 # every 5 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'streams.cron.CheckSubscriptions'    # a unique code

    def do(self):
        subscription_instance = Subscriptions.objects.filter(status=True)
        for x in subscription_instance:
            a = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            c = (x.sub_info).strftime("%d/%m/%Y, %H:%M:%S")
            if a>c:
                x.status = False
                x.save()
        return 0
