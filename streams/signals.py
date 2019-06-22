from django.shortcuts import get_object_or_404
from .models import Subscriptions,LiveStream
from users.models import CustomUser
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
 
 
@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        customdata = ipn.custom
        a = customdata.split("|")
        email = CustomUser.objects.get(email=a[1])
        live_stream_details = LiveStream.objects.get(uid=a[2])
        new_subscription_instance = Subscriptions(uid_id=live_stream_details.id,user_id=email.id,orderid=a[0],status=True,name=live_stream_details.name)
        new_subscription_instance.save()
