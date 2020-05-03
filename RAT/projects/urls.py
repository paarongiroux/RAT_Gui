from django.conf.urls import url, include
from projects.views import ProjectView

urlpatterns = [

	url(r'^$', ProjectView.as_view(), name='rat'),
    url(r'^select2/', include('django_select2.urls')),
    # path("", views.project_index, name="project_index"),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
	# path("", views.firstfloor_index, name="firstfloor_index"),
]
