from django.db import models
from django.contrib.auth import get_user_model
from shared.models import TimestampMixins


User = get_user_model()


class Doctor(TimestampMixins):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    visiting_fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"ID: {self.pk}; User_Id: {self.user_id}; Name: {self.name}"



class Department(TimestampMixins):

    name = models.CharField(max_length=150)
    doctors = models.ManyToManyField(Doctor, related_name='departments')

    def __str__(self):
        return self.name



class Specialization(TimestampMixins):

    name = models.CharField(max_length=150)
    doctors = models.ManyToManyField(Doctor, related_name='specializations')

    def __str__(self):
        return self.name