from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # create crossword
    return render(request, "index.html")
