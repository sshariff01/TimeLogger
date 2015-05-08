from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    hours_worked = models.DecimalField(
            decimal_places=1,
            max_digits=4,
            validators=[
                MaxValueValidator(10),
                MinValueValidator(0.5)
            ],
            default=0
        )