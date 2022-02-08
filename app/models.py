import uuid
from random import getrandbits
from dateutil.relativedelta import relativedelta

from django.db import models

STATUS_CHOICES = [
    ("activated", "active"),
    ("inactivated", "inactive"),
    ("expired", "expired"),
]


class Card(models.Model):
    owner_name = models.CharField(max_length=120)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES)
    issue_date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(unique=True, max_length=120)

    def save(self, *args, **kwargs):
        self.number = str(getrandbits(46))
        super(Card, self).save(*args, **kwargs)

    @property
    def expiration_date(self):
        return self.issue_date + relativedelta(months=18)

    def __str__(self):
        return self.number


class Purchase(models.Model):
    good = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    cc_number = models.ForeignKey('app.Card', on_delete=models.CASCADE, related_name='purchases')

    def __str__(self):
        return f'{self.cc_number}: {self.good}'


# Create your models here.
