from django.db import models



class Subscriber(models.Model):
    """
    creates a table of subscribers that have signed up to ongoing newsletter
    """

    email = models.EmailField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email