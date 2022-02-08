from ..models import Card, STATUS_CHOICES
from datetime import date


def make_expired():
    today = date.today()
    for card in Card.objects.all():
        if today >= card.expiration_date.date():
            card.status = STATUS_CHOICES[2][0]
            card.save()
            print(f'card {card.number} is expired.')
