from django.db import models
from django.utils import timezone

class Person(models.Model):
    HUMAN_TYPE = [
        ("M", "MAN"),
        ("F", "FEMALE"),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/images/")
    type = models.CharField(max_length=2, choices=HUMAN_TYPE)
    date_added = models.DateField(default=timezone.now)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname
