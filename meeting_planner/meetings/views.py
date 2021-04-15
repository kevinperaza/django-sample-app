from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Meeting, Room


def meeting_details(req, id):
    meeting = get_object_or_404(Meeting, pk=id)

    return render(req, "meetings/details.html", {"meeting": meeting})


def rooms_list(req):
    return render(req, "rooms/rooms_list.html", {"rooms": Room.objects.all()})


def room_details(req, id):
    room = get_object_or_404(Room, pk=id)

    return render(req, "rooms/details.html", {"room": room})
