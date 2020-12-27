from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # create crossword
    crossword = create_crossword()
    clues = {"across": ["clue", "clue", "clue"], "down": ["clue", "clue", "clue"]}
    return render(request, "index.html", {"crossword": crossword, "clues": clues})


def create_crossword():
    # generate theme
    # create 4 long words for theme
    # place on grid symmetrically
    # add empty blocks:
    # symmetrically
    # words must be 3+ letters
    # max 78 words in grid
    # make sure all non empty spaces are somehow continuous
    # fill all the words
    crossword = [
        ["M", "A", "I", "N", "E", "", "I", "T", "S", "", "E", "L", "S", "A", ""],
        ["O", "L", "M", "O", "S", "", "D", "I", "E", "", "N", "O", "T", "R", "E"],
        ["J", "O", "H", "N", "Q", "U", "I", "N", "C", "Y", "A", "D", "A", "M", "S"],
        ["O", "T", "O", "", "", "S", "O", "T", "", "E", "M", "O", "T", "E", "S"],
        ["", "", "", "S", "P", "E", "C", "", "E", "S", "E", "", "E", "S", "E"],
        ["Z", "A", "C", "H", "A", "R", "Y", "T", "A", "Y", "L", "O", "R", "", ""],
        ["A", "T", "R", "A", "P", "", "", "H", "R", "E", "", "N", "O", "O", "K"],
        ["R", "O", "A", "M", "", "H", "O", "R", "N", "S", "", "M", "O", "R", "E"],
        ["A", "B", "B", "A", "", "A", "P", "E", "", "", "A", "I", "M", "E", "R"],
        ["", "", "A", "N", "D", "R", "E", "W", "J", "A", "C", "K", "S", "O", "N"],
        ["T", "S", "P", "", "O", "D", "D", "", "A", "N", "T", "E", "", "", ""],
        ["A", "L", "P", "I", "N", "E", "", "A", "B", "A", "", "", "C", "B", "S"],
        ["M", "I", "L", "L", "A", "R", "D", "F", "I", "L", "L", "M", "O", "R", "E"],
        ["S", "M", "E", "L", "T", "", "O", "R", "R", "", "E", "E", "R", "I", "E"],
        ["", "E", "S", "S", "E", "", "S", "O", "U", "", "E", "N", "D", "O", "R"],
    ]
    return crossword