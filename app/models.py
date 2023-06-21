from django.db import models

# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=30)


class Holidays(models.Model):
    date = models.DateField
    type = models.ForeignKey(Type, on_delete=models.SET_DEFAULT, DEFAULT='INNY RODZAJ')
    Notes = models.Text

    def __str__(self):
        return self.type.lower()