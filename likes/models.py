from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Group(models.Model):
    member=models.ForeignKey(Person, on_delete=models.CASCADE)
    like=models.IntegerField(default=0)
    text=models.CharField(max_length=100)

    def __str__(self):
        return self.text
