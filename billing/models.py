from django.db import models
from django.contrib.auth import get_user_model
from shared.models import TimestampMixins
from doctor.models import Doctor
from appointment.models import Appointment



User = get_user_model()



class Billing(TimestampMixins):

    patient_id = models.ForeignKey(User, related_name='patient_billings', on_delete=models.SET_NULL, null=True, blank=True)
    doctor_id = models.ForeignKey(Doctor, related_name='doctor_billings', on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.OneToOneField(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient: {self.patient_id}; Doctor: {self.doctor_id}; Total: {self.total_amount}"