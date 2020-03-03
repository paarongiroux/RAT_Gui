from django.shortcuts import render
from projects.models import *

def project_index(request):
	projects = Project.objects.all()
	firstfloor = FirstFloor.objects.all()
	secondfloor = SecondFloor.objects.all()
	thirfloor = ThirdFloor.objects.all()
	context = {
	 'projects': projects,
	 'firstfloor': firstfloor,
	 'thirdfloor': firstfloor,
	 'thirdfloor': firstfloor
	}
	return render(request, 'project_index.html', context)
