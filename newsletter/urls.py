from django.urls import path
from . import views


urlpatterns = [
    path('subscriber', views.subscriber_signup, name='subscriber'),
]