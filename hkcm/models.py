from __future__ import unicode_literals

from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Cmdata(models.Model):
    issuetime = models.DateTimeField(null=True)
    district = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200)
    crime = models.CharField(max_length=50)
    crimecat = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    title = models.CharField(max_length=500, unique=True)
    URL = models.CharField(max_length=2000)

    class Meta:
        unique_together = ('title', 'crime')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.issuetime >= timezone.now() - datetime.timedelta(days=3)


@python_2_unicode_compatible
class DistrictsForAllLocationsinLocaList(models.Model):
    location = models.CharField(max_length=200, unique=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    Districts = models.CharField(max_length=200)

    def __str__(self):
        return self.location


@python_2_unicode_compatible
class DistrictsClassification(models.Model):
    id_in_cmdata = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    Districts = models.CharField(max_length=200)

    def __str__(self):
        return self.Districts


@python_2_unicode_compatible
class HongKongEighteenDistricts(models.Model):
    Districts = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.Districts


@python_2_unicode_compatible
class latlngMappingDistricts(models.Model):
    id_in_d = models.FloatField(null=True)
    # location = models.CharField(max_length=200, unique=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    Districts = models.CharField(max_length=200)
    # Districts_chn = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.location
