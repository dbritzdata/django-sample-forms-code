from . import views
from django.urls import path

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),  # This line makes /tourist_attractions/ work
    path('state/create', views.StateCreate.as_view(), name="statecreate"),
    path('attraction/create', views.AttractionCreate.as_view(), name="attractioncreate"),
    path("details/<statename>", views.details, name="details"),
    
]
