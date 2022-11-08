import sys
from tkinter import *
import tkinter as tk
import sqlite3
import view
from view.abiadurak import abiadurak
from view.administratzaileLeihoa import administratzaileLeihoa

from controller import konexioa

class saioaHasi(object):

    def __init__(self):
        super(saioaHasi, self).__init__()
        self.window = tk.Tk()
        self.window.title("Saioa hasteko orria")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        con = sqlite3.connect("datubasea.db") #konexioa ezarri
        self.cur = con.cursor()

        Erregistroa = tk.Label(self.window, text="SAIOA HASTEKO ORRIA", bg='CadetBlue1', font=("Times", 14, "bold"))
        Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.erabiltzaileaL = tk.Label(self.window, text="Erabiltzailea:", bg='CadetBlue1', font=("Times", 11))
        self.erabiltzaileaL.place(x=80, y=70)

        self.erabiltzaileaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, validate="key")
        self.erabiltzaileaE.pack(pady=5, padx=5, ipadx=20)

        self.pasahitzaL = tk.Label(self.window, text="Pasahitza:", bg='CadetBlue1', font=("Times", 11))
        self.pasahitzaL.place(x=80, y=100)

        self.pasahitzaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, show="•")
        self.pasahitzaE.pack(pady=5, padx=5, ipadx=20)

        tk.Button(
            self.window,
            text="Saioa hasi",
            padx=10,
            pady=5,
            bg="AliceBlue",
            command=self.printValue
        ).pack(pady=20)

        tk.Button(self.window, text="Itzuli", padx=10, pady=5, bg="AliceBlue", command=self.atzera).pack(pady=10)


        #lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)

        self.window.mainloop()


    def atzera(self):
        self.window.destroy()
        view.ongietorrileioa.ongietorrileioa().__init__()

    def printValue(self):
        erabiltzailea=self.erabiltzaileaE.get()
        pasahitza=self.pasahitzaE.get()

        if ((len(erabiltzailea)!=0) &(len(pasahitza)!=0 )):
            #begiratu saio hastea ondo egin den
            pasahitza2=konexioa.erabiltzailearenPasahitza(konexioa(),erabiltzailea)


            if pasahitza is None: #erabiltzailea ez dago dban
                tk.Label(self.window, text='Erabiltzailea ez da egokia, saiatu berriz mesedez.', pady=10,
                         padx=90, bg='CadetBlue1',
                         font=("Times", 14, "bold")).place(relx=.5, rely=.7, anchor=CENTER)
            else:
                if pasahitza2!=pasahitza: #Idatzitako pasahitza ez dagokio erabiltzaile orri
                    tk.Label(self.window, text='Pasahitza ez dago ondo, saiatu berriz mesedez.',
                             pady=10,
                             padx=90, bg='CadetBlue1',
                             font=("Times", 14, "bold")).place(relx=.5, rely=.7, anchor=CENTER)
                else: #Idatzitako pasahitza dagokio erabiltzaile orri
                    if (erabiltzailea == 'admin'):
                        self.window.destroy()
                        view.administratzaileLeihoa.administratzaileLeihoa().__init__()
                    else:
                        self.window.destroy()
                        view.abiadurak.abiadurak().__init__()



        else:
            tk.Label(self.window, text='Bete itzazu eremu guztiak mesedez.', pady=10,padx=90, bg='CadetBlue1',font=("Times", 14, "bold")).place(relx=.5, rely=.7,anchor= CENTER)




