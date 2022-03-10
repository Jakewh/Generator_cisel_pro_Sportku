import tkinter as tk
from tkinter import *
import sys
import random


""" 
                      _   _         
 ___ _ __   ___  _ __| |_| | ____ _ 
/ __| '_ \ / _ \| '__| __| |/ / _` |
\__ \ |_) | (_) | |  | |_|   < (_| |
|___/ .__/ \___/|_|   \__|_|\_\__,_|
    |_|                             
                                                               
"""
okno = tk.Tk()
okno.title("Generátor tiketů")

def cely():
    top = tk.Toplevel()
    cisla = list(range(1,50))
    Label(top, text=("Sloupec 1", random.sample(cisla, 6))).grid(row=0, column=0, sticky="w")
    Label(top, text=("Sloupec 2", random.sample(cisla, 6))).grid(row=1, column=0, sticky="w")
    Label(top, text=("Sloupec 3", random.sample(cisla, 6))).grid(row=2, column=0, sticky="w")
    Label(top, text=("Sloupec 4", random.sample(cisla, 6))).grid(row=3, column=0, sticky="w")
    Label(top, text=("Sloupec 5", random.sample(cisla, 6))).grid(row=4, column=0, sticky="w")
    Label(top, text=("Sloupec 6", random.sample(cisla, 6))).grid(row=5, column=0, sticky="w")
    Label(top, text=("Sloupec 7", random.sample(cisla, 6))).grid(row=6, column=0, sticky="w")
    Label(top, text=("Sloupec 8", random.sample(cisla, 6))).grid(row=7, column=0, sticky="w")
    Label(top, text=("Sloupec 9", random.sample(cisla, 6))).grid(row=8, column=0, sticky="w")
    Label(top, text=("Sloupec 10", random.sample(cisla, 6))).grid(row=9, column=0, sticky="w")

def sloupec():
    top = tk.Toplevel()
    cisla = list(range(1,50))
    Label(top, text=random.sample(cisla, 6)).grid(row=0, column=0)

Label(okno, text="Co chceš losovat?\n").grid(row=0, column=0, columnspan=2, sticky="we")
cely = tk.Button(okno, text="Celý tiket", command=cely).grid(row=1, column=0)
sloupec = tk.Button(okno, text="Pouze sloupec", command=sloupec).grid(row=1, column=1)

okno.mainloop()

