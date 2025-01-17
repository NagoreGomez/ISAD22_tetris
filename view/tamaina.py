import sys
import tkinter as tk

import view
from view.JokatuLeihoa import JokatuLeihoa




abiadura=0

class tamaina(object):


    def __init__(self,abiadura2, erabiltzailea):
        super(tamaina,self).__init__()
        self.erabiltzailea = erabiltzailea
        self.window = tk.Tk()
        self.window.title("Ongi Etorri!")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.abiadura = abiadura2
        global abiadura
        abiadura = self.abiadura

        self.aukera = tk.IntVar()
        self.aukera.set(value=1)

        self.Erregistroa = tk.Label(self.window, text="TAMAINA HAUTATU", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Radiobutton(self.window, text="10x20 TAMAINA ",padx=40,pady=5, variable=self.aukera, value=1)
        button.pack(pady=10)
        button1 = tk.Radiobutton(self.window, text="15x25 TAMAINA",padx=40,pady=5,variable=self.aukera, value=2)
        button1.pack(pady=10)
        button2 = tk.Radiobutton(self.window, text="20x30 TAMAINA",padx=40,pady=5,variable=self.aukera, value=3)
        button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Hautatu", padx=30, pady=5, command=self.jokatu)
        button3.pack(pady=10)
        button4 = tk.Button(self.window, text="Itzuli", padx=30, pady=5, command=self.itzuli)
        button4.pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def jokatu(self):
        self.window.destroy()
        tamainax = 0
        tamainay = 0
        if (self.aukera.get() == 1):
            tamainax = 10
            tamainay = 20
        elif (self.aukera.get() == 2):
            tamainax = 15
            tamainay = 25
        elif (self.aukera.get() == 3):
            tamainax = 20
            tamainay = 30

        puntuak=0
        partida=None
        view.JokatuLeihoa.JokatuLeihoa(abiadura,tamainax, tamainay,self.erabiltzailea,puntuak, partida ).__init__()

    def itzuli(self):
        self.window.destroy()
        view.abiadurak.abiadurak(self.erabiltzailea).__init__()

