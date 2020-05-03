from django.db import models

# Create your models here.

class Project(models.Model):
   floorNo = models.IntegerField()
   xLocation = models.IntegerField()
   yLocation = models.IntegerField()
   status = models.CharField(max_length=20)
   timestamp = models.DateTimeField(auto_now=True)


class FirstFloor(models.Model):
   room = models.IntegerField()

class SecondFloor(models.Model):
   room = models.IntegerField()

class ThirdFloor(models.Model):
   room = models.IntegerField()

class Floor(models.Model):
   floorNo = models.IntegerField()
   floorname = models.CharField(max_length=255)
   def __str__(self):
      return self.floorname

class Room(models.Model):
   floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
   roomNo = models.IntegerField()
   roomname = models.CharField(max_length=255)

   def __str__(self):
      return self.roomname

