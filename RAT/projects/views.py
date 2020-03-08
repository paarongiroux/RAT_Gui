from django.views.generic import TemplateView
from django.shortcuts import render
from projects.forms import LocationForm
from projects.models import *


class ProjectView(TemplateView):
	template_name = "project_index.html"

	def get(self, request):
		proj = Project.objects.get(id=1)
		proj.xLocation = proj.xLocation + 1
		proj.save()
		projects = Project.objects.all()
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

		context = {
			'projects': projects,
			'form': form,
			'room': room,
			'floor': floor
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
