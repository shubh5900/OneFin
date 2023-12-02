from django.db import models

class Reg(models.Model):
    Name=models.CharField(max_length=100)
    FatherName=models.CharField(max_length=100)
    MotherName=models.CharField(max_length=100)
    Age=models.DateField()
    Gender=models.CharField(max_length=10)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Name} {" "} {self.Email}'
