from django.shortcuts import render
from django.contrib import messages
from newsletter.models import Subscriber
from .forms import SubscriberSignUpForm


def index(request):
    form = SubscriberSignUpForm
    """ A view to return the index page """
    if request.method == 'POST':
        form = SubscriberSignUpForm(request.POST)
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
        else:
            for error in form.errors:
                print(error)

        context = {
            'form': form,
        }

        template = 'newsletter/subscriber.html'

        return render(request, template, context)
    context = {
            'form': form,
        }
    return render(request, 'home/index.html', context)
