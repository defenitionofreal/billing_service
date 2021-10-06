from django.db import models


class Billing(models.Model):
    """ Billing model """
    title = models.CharField(max_length=250, unique=True)
    billing = models.DecimalField(
        'Balance', max_digits=15, decimal_places=2, default=0.00)
    is_over_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Transfer(models.Model):
    """ Transfer balance model """
    sender = models.ForeignKey(
        Billing, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Billing, on_delete=models.CASCADE,
                                 related_name='receiver')
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        # receiver = ", ".join((str(obj) for obj in self.receiver.all()))
        return f'From {self.sender} to {self.receiver}. Amount: {self.amount}'
