"""
views for newsletter
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberSignUpForm

def subscriber_signup(request):
    form = SubscriberSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            messages.info(
                request,
                'Sorry, this email is already subscribed to our newsletter!'
                )
        else:
            messages.success(
                request,
                'Your email has been added succesfully to receive our \
                newsletter!'
                )
            instance.save()

    context = {
        'form': form,
    }

    template = 'newsletter/subscriber.html'

    return render(request, template, context)