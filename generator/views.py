from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    response = requests.get('https://raw.githubusercontent.com/doshea/nyt_crosswords/master/2017/02/01.json')
    crossword = response.json()
    print(crossword)
    crossword['grid'] = zip(crossword['grid'], crossword['gridnums'])
    return render(request, "index.html", {"crossword": crossword})
