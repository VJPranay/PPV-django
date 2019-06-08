from django.contrib import admin
from .models import LiveStream,Subscriptions
# Register your models here.

class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ['name','status','uid']

class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ['user','uid','status']



admin.site.register(LiveStream,LiveStreamAdmin)
admin.site.register(Subscriptions,SubscriptionsAdmin)