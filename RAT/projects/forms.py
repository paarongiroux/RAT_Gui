from django import forms
from .models import Floor, Room
from django_select2.forms import ModelSelect2Widget

FLOOR_CHOICES =(
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)

ROOM_CHOICES =(
	("101", "101"),
	("102", "102"),
	("103", "103"),
	("201", "201"),
	("202", "202"),
	("203", "203"),
	("301", "301"),
	("302", "302"),
	("303", "303"),
)



class LocationForm(forms.Form):

	floor = forms.ChoiceField(choices = FLOOR_CHOICES, label = "Floor")  
	room = forms.ChoiceField(choices = ROOM_CHOICES, label = "Room")



#
# class RoomForm(forms.Form):
# 	floor = forms.ChoiceField(choices = ROOM_CHOICES, label = "Room")
# 	room = forms.ChoiceField(choices = ROOM_CHOICES, label = "Room")
