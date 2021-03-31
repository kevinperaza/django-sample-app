from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def welcome(req):
    return HttpResponse("Welcome to the Meeting Planner!")


def date(req):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(req):
    return HttpResponse("This is a sentence about myself.")
