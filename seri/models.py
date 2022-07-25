from django.db import models


class Account(models.Model):
    account_name = models.CharField(max_length=255, blank=False, null=False)


class TestUser(models.Model):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    account = models.ForeignKey(Account, related_name='users', on_delete=models.CASCADE)
