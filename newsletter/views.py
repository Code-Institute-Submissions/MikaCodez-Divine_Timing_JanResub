"""
views for newsletter
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from .models import Subscriber


@login_required
def subscribers(request):
    """
    view to display how many users subscribed for newsletters
    """
    subscriber_list = Subscriber.objects.order_by('-created_on')

    context = {
        'subscriber_list': subscriber_list,
    }
    return render(request, 'newsletter/subscriber.html', context)


@login_required
def add_subscriber(request):
    """
    view to attach subscriber form to the email database
    """
    next_page = request.POST.get('next', '/')

    # gets email from request and generates lists for for further validation
    # clean email data
    email_from_form = request.POST.get("email")
    email_to_lowercase = email_from_form.lower()
    email = email_to_lowercase.strip()

    # validates if both options are checked
    if "subscribed" in request.POST:
        subscribed = True
    else:
        messages.error(
                request,
                'Please mark the option that you wish to subscribe\
                to newsletter')
        return HttpResponseRedirect(next_page)

    if "accepted_privacy_policy" in request.POST:
        accepted_privacy_policy = True
    else:
        messages.error(
                request,
                'Please mark the option that you accept Privacy Policy')
        return HttpResponseRedirect(next_page)

    if Subscriber.objects.filter(email=email).filter(subscribed=True).exists():
        # email already in database and subscribed
        messages.error(
                request,
                f'The email {email} is already in our database')
        return HttpResponseRedirect(next_page)

    elif Subscriber.objects.filter(
                email=email).filter(subscribed=False).exists():
        # email already in database but not subscribed
        current_subscriber = get_object_or_404(Subscriber, email=email)
        current_subscriber.subscribed = True
        current_subscriber.save(update_fields=['subscribed'])
        messages.success(
            request,
            f'Successfully subscribed email {current_subscriber.email}\
                to our newsletter')
        return HttpResponseRedirect(next_page)

    # check if user is in request
    elif "registered_user" in request.POST:
        user_id = request.POST.get("registered_user")
        registered_user = get_object_or_404(User, id=user_id)

        if Subscriber.objects.filter(
                registered_user=registered_user).filter(
                    subscribed=False).exists():
            # user is already in database but not subscribed
            current_subscriber = get_object_or_404(
                Subscriber, registered_user=registered_user)
            current_subscriber.subscribed = True
            current_subscriber.email = email
            current_subscriber.save(update_fields=['subscribed', 'email'])
            messages.success(
                request,
                f'Successfully subscribed email {current_subscriber.email}\
                    to our newsletter')
            return HttpResponseRedirect(next_page)

        elif Subscriber.objects.filter(
                registered_user=registered_user).filter(
                    subscribed=True).exists():
            current_subscriber = get_object_or_404(
                Subscriber, registered_user=registered_user)
            # user already in database and subscribed, but different email
            messages.error(
                request,
                f'You have already registered {current_subscriber.email}\
                    to receive newsletter')
            return HttpResponseRedirect(next_page)

        else:
            # create new subscriber with registered user
            # creates instance of subscriber class
            subscriber = Subscriber(
                email=email,
                subscribed=subscribed,
                accepted_privacy_policy=accepted_privacy_policy,
                registered_user=registered_user
                )
            subscriber.save()
            messages.success(
                request,
                f'Subscribed email {subscriber.email} to the newsletter')
            return HttpResponseRedirect(next_page)

        # user is not in request
    else:
        registered_user = None
        subscriber = Subscriber(
            email=email,
            subscribed=subscribed,
            accepted_privacy_policy=accepted_privacy_policy,
            registered_user=registered_user
            )
        subscriber.save()
        messages.success(
            request,
            f'Subscribed email {subscriber.email} to the newsletter')
        return HttpResponseRedirect(next_page)


@login_required
def unsubscribe(request):
    """
    view to alter email of user to unsubscribed
    """
    if request.method == 'POST':
        next_page = request.POST.get('next', '/')
        email = request.POST.get("email")
        try:
            current_subscriber = Subscriber.objects.get(email=email)
            current_subscriber.subscribed = False
            current_subscriber.save(update_fields=['subscribed'])
            messages.success(
                request,
                f'Successfully unsubscribed email {current_subscriber.email}\
                    from our newsletter')

        except Subscriber.DoesNotExist:
            messages.error(
                request,
                f'The email {email} is not on our list of subscribers')
            return HttpResponseRedirect(next_page)

        return HttpResponseRedirect(next_page)


@login_required
def unsubscribe_registered_user(request):
    """
    view for authorised users to unsubscribe other users
    """

    user = request.user
    if Subscriber.objects.filter(
            registered_user=user).filter(subscribed=True).exists():
        try:
            current_subscriber = Subscriber.objects.get(registered_user=user)
            current_subscriber.subscribed = False
            current_subscriber.save(update_fields=['subscribed'])
            messages.success(
                request,
                f'Successfully unsubscribed email {current_subscriber.email}\
                    from our newsletter')

        except Subscriber.DoesNotExist:
            messages.error(
                request,
                f'The user {user} is not on our list of subscribers')
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')