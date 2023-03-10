from django import forms
from .models import Subscriber


class SubscriberSignUpForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email