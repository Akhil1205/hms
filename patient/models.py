from django.db import models
from django.core.validators import RegexValidator

from hospital.models import hospital,department


class patient(models.Model):

    mobileNumber_validator = RegexValidator(
        regex=r'^[1-9]\d{9}$',
        message="10 digit number"
    )

    status_enum = [('primary check','primary check'),('consultation','consultation'),('admitted','admitted'),('discharged','discharged')]
    
    patient_name = models.CharField(max_length=50)
    dateofbirth = models.DateField(blank=True,null=True)
    disease= models.CharField(max_length=50)
    mobileNumber = models.DecimalField(max_digits=10,decimal_places=0)
    status = models.CharField(max_length=20,choices=status_enum , default="consultation")
    def _str_(self):
        return self.name

class visited_time(models.Model):

    status_enum = [('primary check','primary check'),('consultation','consultation'),('admitted','admitted'),('discharged','discharged')]

    # id = models.AutoField(auto_created=True,primary_key = True)
    mobileNumber = models.ForeignKey(patient,on_delete=models.CASCADE,unique=True)
    visit_datetime = models.DateTimeField(auto_now=True)
    

    