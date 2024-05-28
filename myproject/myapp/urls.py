from django.urls import path
from .views import*
urlpatterns = [
    
    path("home/",home,name="homepage"),
    path("reg/",studreg,name="studentregister"),
    path("viewstud/",view_stud,name="studentview"),
    path("update/<int:id>/",studupdate,name="studentupdate"),
    path("delete/<int:id>/",deletestud,name="deletestudent")
]