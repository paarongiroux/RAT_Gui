from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Project, FirstFloor, SecondFloor, ThirdFloor, Floor, Room

admin.site.register(Project)
admin.site.register(FirstFloor)
admin.site.register(SecondFloor)
admin.site.register(ThirdFloor)
admin.site.register(Floor)
admin.site.register(Room)