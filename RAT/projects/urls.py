from django.conf.urls import url
from projects.views import ProjectView
# import settings

urlpatterns = [

	url(r'^$', ProjectView.as_view(), name='rat'),

    # path("", views.project_index, name="project_index"),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
	# path("", views.firstfloor_index, name="firstfloor_index"),
]
