# rest
from rest_framework import serializers
# core
from .models import Transfer, Billing
# logic
from .utils.transfer import make_transfer


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['id', 'title', 'billing', 'is_over_draft']


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'sender', 'receiver', 'amount']

    def create(self, validated_data):
        sender = validated_data["sender"]
        receiver = validated_data["receiver"]
        amount = validated_data["amount"]
        make_transfer(sender, receiver, amount)
        return super().create(validated_data)
