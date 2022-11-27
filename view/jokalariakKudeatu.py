import sqlite3
import sys
import tkinter as tk

from tkinter import *
from tkinter import ttk

import view.erabiltzaileLeihoa
#from view.JokatuLeioa import JokatuLeioa
from controller.konexioa import Konexioa

class jokalariakKudeatu(object):


    def __init__(self,erabiltzailea):
        super(jokalariakKudeatu,self).__init__()
        self.window = tk.Tk()
        self.erabiltzailea=erabiltzailea
        self.window.title("Jokalariak kudeatzeko menua")
        self.window.geometry('1000x400')
        self.window['bg'] = 'CadetBlue1'



        self.Erregistroa = tk.Label(self.window, text="JOKALARIAK KUDEATZEKO ORRIA", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.aukera = tk.StringVar()
        self.aukera.set(value=" ")


        # taularen goiko aldea
        self.t1 = tk.Label(self.window, text="Erabiltzailea", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t1.place(x=10, y=70)

        self.t2 = tk.Label(self.window, text="Izen Abizenak", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t2.place(x=150, y=70)

        self.t3 = tk.Label(self.window, text="Helbide elektronikoa", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t3.place(x=300, y=70)

        self.t4 = tk.Label(self.window, text="Pasahitza", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t4.place(x=500, y=70)

        self.t5 = tk.Label(self.window, text="Gako galdera", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t5.place(x=600, y=70)

        self.t6 = tk.Label(self.window, text="Gakoa", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t6.place(x=750, y=70)

        # botoia
        res = Konexioa.getErabiltzailea(Konexioa())
        i = 100
        for row in res:
            self.botoia = tk.Radiobutton(self.window, variable=self.aukera, value=row, bg='CadetBlue1',font=("Times", 12))
            self.botoia.place(x=900, y=i)
            i = i + 30

            # self.i=self.i+1


        #erabiltzailea

        res = Konexioa.getErabiltzailea(Konexioa())
        i = 100
        for row in res:
            #self.l=tk.Label(self.window,text=row)
            #self.l.pack(pady=5)
            self.erab=tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.erab.place(x=10, y=i)
            i=i+30
            #self.i=self.i+1


        #izena
        res = Konexioa.getIzena(Konexioa())
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=150, y=i)
            i = i + 30

        # email
        res = Konexioa.getEmail(Konexioa())
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=300, y=i)
            i = i + 30

        # pasahitza
        res = Konexioa.getPasahitza(Konexioa())
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=500, y=i)
            i = i + 30

        # galko galdera
        res = Konexioa.getGakoGaldera(Konexioa())
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=600, y=i)
            i = i + 30

        # gakoa
        res = Konexioa.getGako(Konexioa())
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=750, y=i)
            i = i + 30

        button2 = tk.Button(self.window,text="Ezabatu",padx=40,pady=5,command=self.ezabatu)
        button2.place(x=400, y=i+40)

        button3 = tk.Button(self.window,text="Itzuli",padx=40,pady=5,command=self.atzera)
        button3.place(x=410, y=i+80)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def ezabatu(self):
        erab = self.aukera.get()
        res=Konexioa.erabiltzaileaKonprobatu(Konexioa(),erab)
        if(res is None):
            print("Erabiltzailea ez dago datu basean")
        else:
            Konexioa.ezabatuErabiltzailea(Konexioa(),erab)
            self.window.destroy()
            jokalariakKudeatu().__init__()



    def atzera(self):
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea)