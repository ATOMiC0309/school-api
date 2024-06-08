from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    classes = models.ManyToManyField(Class)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}. {self.classes}"
