from django.db import models
from django.urls import reverse

# Create your models here.
# models.py
from django.db import models

class department(models.Model):
    # choices = [
    #     ("cardi", "Cardiology"),
    #     ("gastro", "Gastroenterology"),
    #     ("pyschi", "Psychiatry"),
    #     ("hameo", "Haematology"),
    #     ("cc", "Critical Care"),
    #     ("surg", "Surgeon"),
    # ]

    dept_name = models.CharField(max_length=70)

    # def get_dept_name(self):
    #     for short_form,dept_name in self.choices:
    #         if short_form==self.dept_name:
    #             return dept_name
    #     return " "


class hospital(models.Model):
    department=models.ManyToManyField(department)
    hospital_name=models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('update-hospital', kwargs={"id":self.id})
