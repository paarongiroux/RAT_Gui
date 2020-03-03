from django.db import models

# Create your models here.

class Project(models.Model):
   floorNo = models.IntegerField()
   xLocation = models.IntegerField()
   yLocation = models.IntegerField()
   status = models.CharField(max_length=20)
   image = models.FilePathField(path="/img")


class FirstFloor(models.Model):
   room = models.IntegerField()

class SecondFloor(models.Model):
   room = models.IntegerField()

class ThirdFloor(models.Model):
   room = models.IntegerField()
