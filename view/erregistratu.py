import tkinter as tk
from tkinter import ttk, CENTER
from tkinter import *

import sqlite3


class erregistratu(object):

    def __init__(self):
        super(erregistratu, self).__init__()
        self.window = tk.Tk()
        self.window.title("Erregistratzeko orria")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'



        erregistroa = tk.Label(self.window, text="ERREGISTRATZEKO ORRIA",bg='CadetBlue1', font=("Times", 14, "bold"))
        erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        izenaL = tk.Label(self.window, text="Izen Abizenak:",bg='CadetBlue1', font=("Times", 11))
        izenaL.place(x=80, y=70)

        self.izenaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.izenaE.pack(pady=5, padx=5, ipadx=20)

        erabiltzaileaL = tk.Label(self.window, text="Erabiltzailea:",bg='CadetBlue1', font=("Times", 11))
        erabiltzaileaL.place(x=80, y=100)

        self.erabiltzaileaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, validate="key")
        self.erabiltzaileaE.pack(pady=5, padx=5, ipadx=20)

        emailL = tk.Label(self.window, text="Helbide elektronikoa:",bg='CadetBlue1', font=("Times", 11))
        emailL.place(x=80, y=130)

        self.emailE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.emailE.pack(pady=5, padx=5, ipadx=20)

        pasahitzaL = tk.Label(self.window, text="Pasahitza:",bg='CadetBlue1', font=("Times", 11))
        pasahitzaL.place(x=80, y=160)

        self.pasahitzaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, show="•")
        self.pasahitzaE.pack(pady=5, padx=5, ipadx=20)

        gakoaL = tk.Label(self.window, text="Berreskurapen-gakoa:",bg='CadetBlue1', font=("Times", 11))
        gakoaL.place(x=80, y=190)

        self.gakoaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, show="•")
        self.gakoaE.pack(pady=5, padx=5, ipadx=20)

        tk.Button(self.window,text="Erregistratu",padx=10,pady=5,bg="AliceBlue",command=self.printValue).pack(pady=20)


        self.window.mainloop()

    def printValue(self):


        con = sqlite3.connect("datubasea.db")  # konexioa ezarri
        cur = con.cursor()


        izena = self.izenaE.get()
        erabiltzailea=self.erabiltzaileaE.get()
        email=self.emailE.get()
        pasahitza=self.pasahitzaE.get()
        gakoa=self.gakoaE.get()
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        if ((len(izena)!=0 )&(len(erabiltzailea)!=0) &(len(email)!=0 )&(len(pasahitza)!=0 )&(len(gakoa)!=0 )):
            #begiratu erabiltzaile egokia sortu duen
            cur.execute(
                "CREATE TABLE IF NOT EXISTS Erabiltzaileak(erabiltzailea, IzenAbizenak, helbideElektronikoa, pasahitza,gakoa)")
            res = cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
            ezDago = res.fetchone() is None
            if (ezDago):
                tk.Label(self.window, text=f'{izena}, erregistratu zara!', pady=10, padx=180,font=("Times", 14, "bold"), bg='CadetBlue1').place(relx=.5,rely=.8,anchor=CENTER)
                # insert
                cur.execute("INSERT INTO Erabiltzaileak VALUES(?, ?, ?,?,?)", (erabiltzailea, izena, email, pasahitza,gakoa))
                con.commit()
                print("hola1")


            else:
                print("hola2")
                tk.Label(self.window, text=f'{erabiltzailea} erabiltzailea jadanik dago, idatzi beste bat mesedez.', pady=10, padx=90,font=("Times", 14, "bold"), bg='CadetBlue1').place(relx=.5, rely=.8,anchor=CENTER)
        else:
            print("hola3")
            tk.Label(self.window, text='Bete itzazu eremu guztiak mesedez.', pady=10,padx=90,font=("Times", 14, "bold"), bg='CadetBlue1').place(relx=.5, rely=.8,anchor=CENTER)

