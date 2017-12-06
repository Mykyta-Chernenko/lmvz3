from django.core.validators import MaxValueValidator
from django.db import models


class Donor(models.Model):
    RH_CHOICES = (
        ('+','+'),
        ('-','-'),
    )
    BLOOD_GROUP_CHOCIES =(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    birthday = models.DateField()
    blood_group = models.CharField(max_length=1, choices=BLOOD_GROUP_CHOCIES)
    rh = models.CharField(max_length=1, choices=RH_CHOICES)
    diseases = models.TextField()
    pass_date = models.DateField(auto_now_add=True)
