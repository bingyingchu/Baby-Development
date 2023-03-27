from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    week = models.IntegerField()
    choice = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
