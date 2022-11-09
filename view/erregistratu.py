import sys
import tkinter as tk
from tkinter import *
import view
import sqlite3
from controller import konexioa


class erregistratu(object):

    def __init__(self):
        super(erregistratu, self).__init__()
        self.window = tk.Tk()
        self.window.title("Erregistratzeko orria")
        self.window.geometry('600x500')
        self.window['bg'] = 'CadetBlue1'



        erregistroa = tk.Label(self.window, text="ERREGISTRATZEKO ORRIA",bg='CadetBlue1', font=("Times", 14, "bold"))
        erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        izenaL = tk.Label(self.window, text="Izen Abizenak:",bg='CadetBlue1', font=("Times", 11))
        izenaL.place(x=75, y=70)

        self.izenaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.izenaE.pack(pady=5, padx=5, ipadx=20)

        erabiltzaileaL = tk.Label(self.window, text="Erabiltzailea:",bg='CadetBlue1', font=("Times", 11))
        erabiltzaileaL.place(x=75, y=100)

        self.erabiltzaileaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, validate="key")
        self.erabiltzaileaE.pack(pady=5, padx=5, ipadx=20)

        emailL = tk.Label(self.window, text="Helbide elektronikoa:",bg='CadetBlue1', font=("Times", 11))
        emailL.place(x=75, y=130)

        self.emailE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.emailE.pack(pady=5, padx=5, ipadx=20)

        pasahitzaL = tk.Label(self.window, text="Pasahitza:",bg='CadetBlue1', font=("Times", 11))
        pasahitzaL.place(x=75, y=160)

        self.pasahitzaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, show="•")
        self.pasahitzaE.pack(pady=5, padx=5, ipadx=20)

        gakoGalderaL = tk.Label(self.window, text="Berreskurapen-galdera:",bg='CadetBlue1', font=("Times", 11))
        gakoGalderaL.place(x=75, y=190)

        self.gakoGalderaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.gakoGalderaE.pack(pady=5, padx=5, ipadx=20)

        gakoaL = tk.Label(self.window, text="Berreskurapen-gakoa:", bg='CadetBlue1', font=("Times", 11))
        gakoaL.place(x=75, y=220)

        self.gakoaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.gakoaE.pack(pady=5, padx=5, ipadx=20)

        tk.Button(self.window,text="Erregistratu",padx=10,pady=5,bg="AliceBlue",command=self.printValue).pack(pady=15)


#atzera
        tk.Button(self.window, text="Itzuli", padx=10, pady=5, bg="AliceBlue", command=self.itzuli).pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def itzuli(self):
        self.window.destroy()
        view.ongietorrileioa.ongietorrileioa().__init__()


    def printValue(self):


        con = sqlite3.connect("datubasea.db")  # konexioa ezarri
        cur = con.cursor()


        izena = self.izenaE.get()
        erabiltzailea=self.erabiltzaileaE.get()
        email=self.emailE.get()
        pasahitza=self.pasahitzaE.get()
        gakoa=self.gakoaE.get()
        gakoGaldera=self.gakoGalderaE.get()
        if ((len(izena)!=0 )&(len(erabiltzailea)!=0) &(len(email)!=0 )&(len(pasahitza)!=0 )&(len(gakoGaldera)!=0 ) & (len(gakoa)!=0 )):
            erab2=konexioa.erabiltzaileaKonprobatu(konexioa(),erabiltzailea)
            if erab2 is None:
                konexioa.erabiltzaileaGehitu(konexioa(),izena,erabiltzailea,email,pasahitza,gakoa,gakoGaldera)
                self.window.destroy()
                view.saioaHasi.saioaHasi().__init__()

            else:
                tk.Label(self.window, text=f'{erabiltzailea} erabiltzailea jadanik dago, idatzi beste bat mesedez.',
                         pady=10, padx=90, font=("Times", 14, "bold"), bg='CadetBlue1').place(relx=.5, rely=.8,
                                                                                              anchor=CENTER)
        else:
            tk.Label(self.window, text='Bete itzazu eremu guztiak mesedez.', pady=10, padx=90,
                     font=("Times", 14, "bold"), bg='CadetBlue1').place(relx=.5, rely=.8, anchor=CENTER)


