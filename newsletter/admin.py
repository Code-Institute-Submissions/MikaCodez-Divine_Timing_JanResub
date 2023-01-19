from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    '''
    class enabling admin see the Subscriber model in admin panel
    '''
    list_display = ('email', 'date_added')
