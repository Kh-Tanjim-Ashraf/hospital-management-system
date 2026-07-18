from django.db import models
from django.contrib.auth import get_user_model
from shared.models import TimestampMixins
from doctor.models import Doctor



User = get_user_model()



class Appointment(TimestampMixins):

    STATUS = [
        ('pend', 'Pending'),
        ('conf', 'Confirmed'),
        ('comp', 'Completed'),
        ('canc', 'Cancelled')
    ]

    patient_id = models.ForeignKey(User, related_name='patients', on_delete=models.SET_NULL, null=True, blank=True)
    doctor_id = models.ForeignKey(Doctor, related_name='doctors', on_delete=models.SET_NULL, null=True, blank=True)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=4, choices=STATUS, default='pend')

    def __str__(self):
        return f"Patient: {self.patient_id}; Doctor: {self.doctor_id}; Status: {self.status}"