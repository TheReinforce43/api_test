from django.db import models

# Create your models here.

class TeacherModel(models.Model):
    Name=models.CharField(max_length=250)
    CourseName=models.CharField(max_length=250)
    Duration=models.IntegerField(default=0)
    Seat=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.Name
