from django.views import generic
from django.shortcuts import render
from streams.models import LiveStream,Subscriptions
from django.shortcuts import get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from django.urls import reverse


def HomePageView(req):
    live_streams_instance = LiveStream.objects.filter(status=True)
    web_page_data = {
        'LiveStreams' : live_streams_instance
    }
    return render(req,template_name='pages/home.html',context=web_page_data)

paypal_dict = { }

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

    def get_context_data(self, **kwargs):
        context = super(StreamDetail, self).get_context_data(**kwargs)
        object = get_object_or_404(LiveStream,uid=self.kwargs['uid'])
        uid=self.kwargs['uid']
        email = self.request.user
        orderid = uuid.uuid4() 
        host = self.request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': Decimal(object.price).quantize(Decimal('.01')),
            'item_name' : object.name,
            'invoice': str(orderid),
            'currency_code': 'USD',
            'custom' : ( str(orderid) + '|' + str(email) + '|' + str(uid) ),
             'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                           reverse('processing_payment')),
            'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_failed')), }
        context['form'] = PayPalPaymentsForm(initial=paypal_dict)
        return context
        
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
        
class PaymentFormView(generic.FormView):
    form_class = PayPalPaymentsForm(initial=paypal_dict)
    success_url = '/about'

# class HomePageView(TemplateView):    
#     template_name = 'pages/home.html'

class ProcessingPayment(generic.ListView):
    model = Subscriptions
    queryset = Subscriptions.objects.filter(status=True)
    context_object_name = 'subscriptions'
    template_name = 'pages/processing_payment.html'

class PaymentFailed(generic.TemplateView):
    template_name = 'pages/payment_failed.html'


class AboutPageView(generic.TemplateView):
    template_name = 'pages/about.html'