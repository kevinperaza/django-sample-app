from django.urls import path
from . import views

urlpatterns = [
    path('meetings/<int:id>', views.meeting_details, name="meeting_details"),
    path('rooms', views.rooms_list, name="rooms_list"),
    path('rooms/<int:id>', views.room_details, name="room_details"),

]
