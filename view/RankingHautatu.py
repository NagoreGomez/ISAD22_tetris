import sqlite3
import sys
import tkinter as tk
from tkinter import *
import view
from view.abiadurak import abiadurak
from controller.konexioa import Konexioa


class RankigHautatu(object):
    def __init__(self,erabiltzailea):
        super(RankigHautatu,self).__init__()
        self.erabiltzailea=erabiltzailea
        self.window = tk.Tk()
        self.window.title("Pertsonalizazio menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.aukeraabsolutua = tk.IntVar()
        self.aukeraabsolutua.set(value=1)

        self.RankigHautatu = tk.Label(self.window, text="RANKIG-A HAUTATU", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.RankigHautatu.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.absolutua = tk.Label(self.window, text="RANKING ABSOLUTUA:", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.absolutua.place(x=100, y=70)

        self.absolutua1 = tk.Radiobutton(self.window,variable=self.aukeraabsolutua, text="BAI",value=1, bg='CadetBlue1', font=("Times", 12))
        self.absolutua1.place(x=100, y=100)

        self.absolutua2 = tk.Radiobutton(self.window, variable=self.aukeraabsolutua, text="MAILAKO BAT", value=2, bg='CadetBlue1', font=("Times", 12))
        self.absolutua2.place(x=200, y=100)


        self.aukeraabiadura = tk.IntVar()
        self.aukeraabiadura.set(value=1)

        self.mailako = tk.Label(self.window, text="MAILAKO RANKIG-AK", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.mailako.place(x=100, y=140)

        self.abiadura = tk.Label(self.window, text="Abiadura:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.abiadura.place(x=100, y=170)

        self.abiadura1 = tk.Radiobutton(self.window,variable=self.aukeraabiadura, text="Motela", value=1, bg='CadetBlue1', font=("Times", 12))
        self.abiadura1.place(x=100, y=190)

        self.abiadura2 = tk.Radiobutton(self.window,variable=self.aukeraabiadura, text="Ertaina",value=2, bg='CadetBlue1', font=("Times", 12))
        self.abiadura2.place(x=200, y=190)

        self.abiadura3 = tk.Radiobutton(self.window,variable=self.aukeraabiadura, text="Azkarra",value=3, bg='CadetBlue1', font=("Times", 12))
        self.abiadura3.place(x=300, y=190)

        self.aukeratamaina = tk.IntVar()
        self.aukeratamaina.set(value=1)

        self.tamaina = tk.Label(self.window, text="Tamaina:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.tamaina.place(x=100, y=230)

        self.tamaina1 = tk.Radiobutton(self.window,variable=self.aukeratamaina, text="10x20", value=1, bg='CadetBlue1', font=("Times", 12))
        self.tamaina1.place(x=100, y=250)

        self.tamaina2 = tk.Radiobutton(self.window,variable=self.aukeratamaina, text="15x25", value=2, bg='CadetBlue1', font=("Times", 12))
        self.tamaina2.place(x=200, y=250)

        self.tamaina3 = tk.Radiobutton(self.window,variable=self.aukeratamaina, text="20x30", value=3, bg='CadetBlue1', font=("Times", 12))
        self.tamaina3.place(x=300, y=250)

        button2 = tk.Button(self.window, text="Ikusi", padx=30, pady=5, command=self.pertsonalizazioa)
        button2.place(x=110, y=300)

        button3 = tk.Button(self.window, text="Itzuli", padx=40, pady=5, command=self.itzuli)
        button3.place(x=310, y=300)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)

        self.window.mainloop()

    def itzuli(self):
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea).__init__()

    def pertsonalizazioa(self):

        self.fondoa="a"

        if (self.aukeraFondoa.get() == 1):
            self.fondoa = "#98F5FF"
        elif (self.aukeraFondoa.get() == 2):
            self.fondoa= "#00C957"
        elif (self.aukeraFondoa.get() == 3):
            self.fondoa = "#FF3030"

        self.adreiluak = "a"
        if (self.aukeraAdreilu.get() == 1):
            self.adreiluak = "1"
        elif (self.aukeraAdreilu.get() == 2):
            self.adreiluak = "2"
        elif (self.aukeraAdreilu.get() == 3):
            self.adreiluak = "3"

        self.soinua = "a"
        if (self.aukeraSoinu.get() == 1):
            self.soinua = "soinua1"
        elif (self.aukeraSoinu.get() == 2):
            self.soinua = "soinua2"
        elif (self.aukeraSoinu.get() == 3):
            self.soinua = "soinua3"


        #guardar en la datubase
        Konexioa.pertsonalizazioaGorde(Konexioa(), self.fondoa,self.adreiluak,self.soinua,self.erabiltzailea)

        #volver al menu
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea).__init__()



