from django.db import models


class Horses(models.Model):
    id = models.IntegerField(primary_key=True)
    genotype = models.CharField(max_length=255, blank=True, null=True)
    bloodline = models.CharField(max_length=255, blank=True, null=True)
    breed_type = models.CharField(max_length=255, blank=True, null=True)
    horse_type = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'horses'
