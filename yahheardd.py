#git pull update from git to pc
#git add adds the things i want to update, in sections. its in a list of things im putting
#git commit -m. grouped up and added a message
#git push
#git pull

import sqlite3 as sql
from tkinter import *
from tkinter import messagebox

try:
    con = sql.connect('pin_your_note.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
except:
    print("oop something went wrong")
    
    
def viewnotes():
    return

def updatenotes():
    return

def deletenotes():
    return 