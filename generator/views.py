from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
import random

def index(request):
    crossword, error = get_crossword()
    if not error:
        crossword['grid'] = zip(crossword['grid'], crossword['gridnums'])
    return render(request, "index.html", {"crossword": crossword, 'error': error})

def get_crossword():
    # get random date
    crossword_date = random_date()
    response = requests.get(f'https://raw.githubusercontent.com/doshea/nyt_crosswords/master/{crossword_date.strftime("%Y/%m/%d")}.json')
    if response.status_code == 200:
        return response.json(), None
    return None, "Woops! Something went wrong - please try again."

def random_date():
    # key dates from GitHub repo: https://github.com/doshea/nyt_crosswords
    start = datetime.datetime(1976, 1, 1)
    end = datetime.datetime(2015, 1, 1)
    start_gap = datetime.datetime(1978, 8, 10)
    end_gap = datetime.datetime(1978, 11, 5)
    
    random_date = start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

    # check generated date isn't in gaps
    if start_gap <= random_date <= end_gap:
        random_date = random_date(start, end)
    return random_date
