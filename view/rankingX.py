import sqlite3
import sys
import tkinter as tk

from tkinter import *
from tkinter import ttk

import view.erabiltzaileLeihoa
#from view.JokatuLeioa import JokatuLeioa
from controller.konexioa import Konexioa

class RankingX(object):


    def __init__(self,erabiltzailea,tamaina, abiadura):
        super(RankingX,self).__init__()
        self.window = tk.Tk()
        self.erabiltzailea=erabiltzailea
        self.window.title("Mailaka ranking")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'




        self.Erregistroa = tk.Label(self.window, text=" MAILAKO RANKING-A IKUSTEKO ORRIA", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.aukera = tk.StringVar()
        self.aukera.set(value=" ")


        # taularen goiko aldea
        self.t1 = tk.Label(self.window, text="Erabiltzailea", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t1.place(x=20, y=70)


        self.t4 = tk.Label(self.window, text="Puntuak", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t4.place(x=200, y=70)


        res=Konexioa.getRankingX(Konexioa(), tamaina,abiadura)

        luzera=len(res)

        i = 100
        unekoPos=0
        while (unekoPos<luzera):
            erabiltzailea,puntuak = res[unekoPos]

            self.erab = tk.Label(self.window, text=erabiltzailea, bg='CadetBlue1', font=("Times", 12))
            self.erab.place(x=20, y=i)

            self.puntuak = tk.Label(self.window, text=puntuak, bg='CadetBlue1', font=("Times", 12))
            self.puntuak.place(x=200, y=i)
            i = i + 30
            unekoPos=unekoPos+1



        button3 = tk.Button(self.window,text="Itzuli",padx=40,pady=5,command=self.atzera)
        button3.place(x=200, y=i+80)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()


    def atzera(self):
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea)