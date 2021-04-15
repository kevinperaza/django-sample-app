from django.shortcuts import render
from meetings.models import Meeting, Room


def welcome(req):
    return render(req, "website/welcome.html", {"meetings": Meeting.objects.all()})
