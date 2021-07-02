from django.db import models
from django.contrib.postgres.fields import ArrayField


class Scale(models.Model):
    family = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default='')
    interval_steps = ArrayField(
        models.FloatField(blank=True, null=True), size=8),
    systematic_name = models.CharField(max_length=255, default='')
    # chords = models.ManyToManyField('Chord', related_name='scales')

    def __str__(self):
        return str(self.title)


# class Chord(models.Model):
#     pass
