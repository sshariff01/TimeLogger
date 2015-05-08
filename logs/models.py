from django.db import models


class Tutor(models.Model):
    name = models.CharField(
        max_length=200
    )
    last_updated = models.DateTimeField(
        auto_now_add=True
    )


class Log(models.Model):
    tutor = models.ForeignKey(Tutor)
    date = models.DateTimeField()
    hours_worked = models.CharField(
        max_length=4
    )