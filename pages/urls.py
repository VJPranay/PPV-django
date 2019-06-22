from django.urls import path

from .views import HomePageView, AboutPageView,StreamDetail,ProcessingPayment,PaymentFailed

urlpatterns = [
    path('', HomePageView, name='home'),
    path('stream/<slug:uid>/', StreamDetail.as_view(), name='stream_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('processing_payment/', ProcessingPayment.as_view(), name='processing_payment'),
    path('payment_failed/', PaymentFailed.as_view(), name='payment_failed'),
]
