import sqlite3
import tkinter as tk
from tkinter import *
import view
from view.abiadurak import abiadurak
from controller.konexioa import Konexioa


class pertsonalizatu(object):
    def __init__(self,erabiltzailea):
        super(pertsonalizatu,self).__init__()
        self.erabiltzailea=erabiltzailea
        self.window = tk.Tk()
        self.window.title("Pertsonalizazio menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.aukeraFondoa = tk.IntVar()
        self.aukeraFondoa.set(value=1)

        self.Pertsonalizazioa = tk.Label(self.window, text="PERTSONALIZAZIO ORRIA", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.Pertsonalizazioa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.atzekoKolorea = tk.Label(self.window, text="Atzeko kolorea:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.atzekoKolorea.place(x=100, y=70)

        self.atzekoKolorea1 = tk.Radiobutton(self.window,variable=self.aukeraFondoa, text="Urdina",value=1, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea1.place(x=100, y=100)

        self.atzekoKolorea2 = tk.Radiobutton(self.window,variable=self.aukeraFondoa, text="Berdea",value=2, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea2.place(x=200, y=100)

        self.atzekoKolorea3 = tk.Radiobutton(self.window,variable=self.aukeraFondoa, text="Gorria",value=3, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea3.place(x=300, y=100)

        self.aukeraAdreilu = tk.IntVar()
        self.aukeraAdreilu.set(value=1)


        self.adreiluKoloreak = tk.Label(self.window, text="Adreilu koloreak:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.adreiluKoloreak.place(x=100, y=150)

        self.atzekoKolorea1 = tk.Radiobutton(self.window,variable=self.aukeraAdreilu, text="Beroak", value=1, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea1.place(x=100, y=180)

        self.atzekoKolorea2 = tk.Radiobutton(self.window,variable=self.aukeraAdreilu, text="Hotzak",value=2, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea2.place(x=200, y=180)

        self.atzekoKolorea3 = tk.Radiobutton(self.window,variable=self.aukeraAdreilu, text="Koloretakoak",value=3, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea3.place(x=300, y=180)

        self.aukeraSoinu = tk.IntVar()
        self.aukeraSoinu.set(value=1)


        self.soinua = tk.Label(self.window, text="Soinua:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.soinua.place(x=100, y=230)

        self.atzekoKolorea1 = tk.Radiobutton(self.window,variable=self.aukeraSoinu, text="Klasikoa", value=1, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea1.place(x=100, y=260)

        self.atzekoKolorea2 = tk.Radiobutton(self.window,variable=self.aukeraSoinu, text="Guitarra", value=2, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea2.place(x=200, y=260)

        self.atzekoKolorea3 = tk.Radiobutton(self.window,variable=self.aukeraSoinu, text="Chundachunda", value=3, bg='CadetBlue1', font=("Times", 12))
        self.atzekoKolorea3.place(x=300, y=260)

        button2 = tk.Button(self.window, text="Pertsonalizazioa gorde", padx=30, pady=5, command=self.pertsonalizazioa)
        button2.place(x=110, y=300)

        button3 = tk.Button(self.window, text="Itzuli", padx=40, pady=5, command=self.itzuli)
        button3.place(x=310, y=300)


        self.window.mainloop()

    def itzuli(self):
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa()

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

        print( self.fondoa)
        print(self.adreiluak)
        print(self.soinua)

        #guardar en la db
        Konexioa.pertsonalizazioaGorde(Konexioa(), self.fondoa,self.adreiluak,self.soinua,self.erabiltzailea)

        #volver al menu
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea).__init__()



