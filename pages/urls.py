from django.urls import path

from .views import HomePageView, AboutPageView,StreamDetail

urlpatterns = [
    path('', HomePageView, name='home'),
    path('stream/<slug:uid>/', StreamDetail.as_view(), name='stream_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]
