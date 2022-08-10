from django.db import models


class Account(models.Model):
    account_name = models.CharField(max_length=255, blank=False, null=False)


class TestUser(models.Model):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    account = models.ForeignKey(Account, related_name='users', on_delete=models.CASCADE)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ('order', )

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)
