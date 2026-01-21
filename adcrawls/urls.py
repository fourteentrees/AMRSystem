from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>/content.txt", views.getcrawlcontent, name="getcrawlcontent"),
    path("<int:id>.json", views.detailjson, name="detailjson"),
]