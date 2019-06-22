from django.db import models
import uuid 
from users.models import CustomUser
from django.utils import timezone
from sorl.thumbnail import ImageField, get_thumbnail
import random
import string


def calculate_expiry_time():
    return timezone.now() + timezone.timedelta(hours=6)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

a = id_generator()

STATUS_CHOICES = (
    (True, ("Start")),
    (False, ("Stop"))
)



# Create your models here.
class LiveStream(models.Model):

    name = models.CharField(max_length=255,blank=True,null=True)
    rtmp_url = models.CharField(max_length=255,default='rtmp://62.210.116.81:1935/show')
    key = models.CharField(max_length=255,default=id_generator)
    description = models.TextField(blank=True,null=True)
    image = ImageField(blank=True,null=True,upload_to="media/stream_cover")
    status = models.BooleanField(blank=True,null=True,choices=STATUS_CHOICES)
    price = models.IntegerField(blank=True,null=True)
    uid = models.CharField(max_length=255,default=uuid.uuid4,blank=True,null=True,editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(LiveStream, self).save(*args, **kwargs)
        self.image = get_thumbnail(self.image, '640x306', crop='center', quality=10, format='JPEG').name
        

    
class Subscriptions(models.Model):
    orderid = models.CharField(unique=True,max_length=255,blank=True,null=True,editable=False)
    user = models.ForeignKey(CustomUser,on_delete=None,blank=True,null=True, )
    uid = models.ForeignKey(LiveStream,on_delete=None,blank=True,null=True,)
    status = models.BooleanField(blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    sub_info = models.DateTimeField(default=calculate_expiry_time,blank=True,null=True)

    def get_uid(self):
        return Subscriptions.objects.get( )