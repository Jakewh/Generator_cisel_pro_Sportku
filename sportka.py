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

# ikona okna
ikona = PhotoImage(file="/home/jakub/GitHub/sportka/ico.png")
okno.iconphoto(True, ikona)

def cely():
    """losování celého tiketu"""
    top = tk.Toplevel()
    cisla = list(range(1,50))
    Label(top, text="Sloupec 1: ").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 2: ").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 3: ").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 4: ").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 5: ").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 6: ").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 7: ").grid(row=6, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 8: ").grid(row=7, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 9: ").grid(row=8, column=0, sticky="e", padx=5, pady=5)
    Label(top, text="Sloupec 10: ").grid(row=9, column=0, sticky="e", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=0, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=1, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=2, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=3, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=4, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=5, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=6, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=7, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=8, column=1, sticky="w", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=9, column=1, sticky="w", padx=5, pady=5)

def sloupec():
    """losování sloupce"""
    top = tk.Toplevel()
    cisla = list(range(1,50))
    Label(top, text="Sloupec: ").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    Label(top, text=random.sample(cisla, 6)).grid(row=0, column=1, sticky="w", padx=5, pady=5)

def info_menu():
    """ Položka "Info" v menu"""
    info_okno = tk.Toplevel()
    info_okno.title("Info")
    Label(info_okno, image=ikona).grid(row=0, column=0, pady=5)
    Label(info_okno, text="Generátor tiketů v0.2.1", font="bold").grid(row=1, column=0, sticky="we", pady=5, padx=5)
    Label(info_okno, text="Jakub Kolář\nkolarkuba@gmail.com\n2021").grid(row=2, column=0, sticky="we", pady=5, padx=5)
    close_button = Button(info_okno,text = "Zavřít",command=lambda:info_okno.destroy()).grid(row=3, column=0, pady=5)

# text hlavního okna
Label(okno, text="\nCo chceš losovat?\n", font="bold").grid(row=0, column=0, columnspan=2, sticky="we")

# menu
mb = Menu(okno)
file_menu = Menu(mb, tearoff=0)
mb.add_command(label="Info", command=info_menu)
okno.config(menu=mb)

# tlačítka
cely = tk.Button(okno, text="Celý tiket", command=cely).grid(row=1, column=0)
sloupec = tk.Button(okno, text="Pouze sloupec", command=sloupec).grid(row=1, column=1)

okno.mainloop()

