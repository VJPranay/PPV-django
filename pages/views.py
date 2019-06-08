from django.views import generic
from django.shortcuts import render
from streams.models import LiveStream,Subscriptions
from django.shortcuts import get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist

def HomePageView(req):
    live_streams_instance = LiveStream.objects.filter(status=True)
    web_page_data = {
        'LiveStreams' : live_streams_instance
    }
    return render(req,template_name='pages/home.html',context=web_page_data)


@method_decorator(login_required, name='dispatch')
class StreamDetail(generic.DetailView):
    model = LiveStream
    slug_field = 'uid'
    template_name = 'pages/stream_detail.html'

    # def check_subcription_status(self):
    #     uid=self.kwargs['uid']
    #     email = self.request.user
    #     try:
    #         a = Subscriptions.objects.get(uid__uid=uid,user__email=email,status=True)
    #         return 1
    #     except ObjectDoesNotExist:
    #         return 0
        
        
    def get_object(self):
        object = get_object_or_404(LiveStream,uid=self.kwargs['uid'])
        uid=self.kwargs['uid']
        email = self.request.user
        try:
            a = Subscriptions.objects.get(uid__uid=uid,user__email=email,status=True)
            return object
        except ObjectDoesNotExist:
            object.status = "Unsubscribed"
            return object
        



# class HomePageView(TemplateView):    
#     template_name = 'pages/home.html'


class AboutPageView(generic.TemplateView):
    template_name = 'pages/about.html'