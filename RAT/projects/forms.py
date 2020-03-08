from django import forms

FLOOR_CHOICES =(
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)

ROOM_CHOICES =(
	("101", "101"),
	("202", "202"),
	("303", "303"),
)



class LocationForm(forms.Form):


	floor = forms.ChoiceField(choices = FLOOR_CHOICES, label = "Floor")  
	room = forms.ChoiceField(choices = ROOM_CHOICES, label = "Room")



#
# class RoomForm(forms.Form):
# 	floor = forms.ChoiceField(choices = ROOM_CHOICES, label = "Room")
# 	room = forms.ChoiceField(choices = ROOM_CHOICES, label = "Room")
