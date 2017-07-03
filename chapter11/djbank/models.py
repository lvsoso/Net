#coding=utf-8

from django.db import models
from django.forms import ModelForm

class Payment(models.Model):
    debit = models.CharField(max_length=200)
    credit = models.CharField(max_length=200, verbose_name='To account')
    dollars = models.PositiveIntegerField()
    memo = models.CharField(max_length=200)


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['credit', 'dollars', 'memo']