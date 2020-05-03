from django.views.generic import TemplateView
from django.shortcuts import render
from projects.forms import LocationForm
from projects.models import *
import random
import socket


class ProjectView(TemplateView):
	template_name = "project_index.html"

	def get(self, request):
		# temp code to show retreival of projects field from database
		#queryset = Project.objects.get()
		#random.seed()
		#randfloor = random.randint(1, 3)
		#proj = Project.objects.get(id=1)
		#proj.xLocation = proj.xLocation + 1
		#proj.floorNo = randfloor
		#proj.save()
		projects = Project.objects.all().order_by('-timestamp')
		# end temp code

		form = LocationForm()
		room = ""
		floor = ""
		context = {
			'projects': projects,
			'form': form,
			'room': room,
			'floor': floor
			}
		return render(request, self.template_name, context)

	def post(self, request):
		form = LocationForm(request.POST)
		if form.is_valid():
			projects = Project.objects.all()
			room = form.cleaned_data['room']
			floor = form.cleaned_data['floor']
			ratIp = 'localhost'
			ratPort = 55555
			#create a socket to the robot and send the room and floor to it
			try:
				soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				soc.connect((ratIp, ratPort))
				newlocation = "%s, %s" %(floor, room)
				soc.send(newlocation.encode('utf-8'))
				soc.shutdown(1)
				soc.close()

			except OSError as err:
				print("Socket failed with error %s" %(err))
			
		context = {
			'projects': projects,
			'form': form,
			'room': room,
			'floor': floor,
			}
		
		return render(request, self.template_name, context)

# from django.shortcuts import render
# from projects.models import *
#
#
#
# def project_index(request):
# 	projects = Project.objects.all()
# 	firstfloor = FirstFloor.objects.all()
# 	secondfloor = SecondFloor.objects.all()
# 	thirfloor = ThirdFloor.objects.all()
# 	context = {
# 	 'projects': projects,
# 	 'firstfloor': firstfloor,
# 	 'thirdfloor': firstfloor,
# 	 'thirdfloor': firstfloor
# 	}
# 	return render(request, 'project_index.html', context)

