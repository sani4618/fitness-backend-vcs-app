from django.urls import path
from . import views

urlpatterns = [
    path('newreg/',views.newregister,name="new"),
    path('viewall/',views.viewfitnessreg,name="viewall")
    
]
