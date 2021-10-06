from ..models import Billing
from rest_framework import serializers

def sender_receiver(sender_data, receiver_data, amount_data):
    sender = sender_data
    receiver = receiver_data
    amount = amount_data

    sender.billing -= amount
    sender.save()
    try:
        one_receiver = Billing.objects.get(title=receiver)
        one_receiver.billing += amount
        one_receiver.save()
    except Billing.DoesNotExist:
        raise serializers.ValidationError(
            'Счета {value} нет в базе.'.format(
                value=receiver
            )
        )

def make_transfer(sender_data, receiver_data, amount_data):
    count_bill = sender_data.billing - amount_data
    if count_bill >= 0:
        sender_receiver(sender_data, receiver_data, amount_data)
    elif sender_data.is_over_draft is True and count_bill < 0:
        sender_receiver(sender_data, receiver_data, amount_data)
    else:
        raise serializers.ValidationError(
            'Не хватает средств'
        )
