#!/usr/bin/env python3
#playerctl open spotify:track:1NM2qI63ylqg62yxpEvTXu
print ("Starting Game...")

from uriformat import *
import openpyxl as xl
from os import system
from random import shuffle

wb = xl.load_workbook(filename = "songlist.xlsx")
ws = wb["Form Responses 1"]

playlist = []

for row in range(2, ws.max_row+1):
    for column in "BCDEFG":
        cell_name = "{}{}".format(column, row)
        if (cell_name[0] == "B"):
            ownername = ws[cell_name].value
        else:
            x = ws[cell_name].value
            if(type(ws[cell_name].value) == int):
               x = str(ws[cell_name].value) + 'a'
            playlist.append(Songlink(URLtoURI(x), ownername))

shuffle(playlist)

songNum = 0
while True:
    command = input("(p)ause, (n)ext song, or (q)uit: ")
    if command == "p":
        system("./sp play")

    if command == "n":
        print(songNum+1)
        print(playlist[songNum].getLink())
        system("./sp open {}".format(playlist[songNum].getLink()))
        songNum+=1

    if command == "q":
        break

for i in range(0, len(playlist)):
    print(playlist[i].getLink(), playlist[i].getOwner())
