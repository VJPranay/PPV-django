from django.db import models
import uuid 
from users.models import CustomUser

STATUS_CHOICES = (
    (True, ("Start")),
    (False, ("Stop"))
)

# Create your models here.
class LiveStream(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    status = models.BooleanField(blank=True,null=True,choices=STATUS_CHOICES)
    uid = models.CharField(max_length=255,default=uuid.uuid4,blank=True,null=True,editable=False)

    def __str__(self):
        return self.name

    
class Subscriptions(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=None,blank=True,null=True, )
    uid = models.ForeignKey(LiveStream,on_delete=None,blank=True,null=True,)
    status = models.BooleanField(blank=True,null=True)
    sub_info = models.DateTimeField(auto_now_add=True,blank=True,null=True)