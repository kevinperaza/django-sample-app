from datetime import time
from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    # add `default` values to make this thing backwards compatible
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    # on delete => sql cascade
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} at {self.start_time} on {self.date}"
