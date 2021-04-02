from django.shortcuts import render
from meetings.models import Meeting


def welcome(req):
    return render(req, "website/welcome.html", {"number_of_meetings": Meeting.objects.count()})
