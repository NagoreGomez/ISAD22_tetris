import sys
from tkinter import *
import tkinter as tk
import view
from model.Jokalariak import Jokalariak
from model.Jokalaria import Jokalaria



class pasahitzaBerreskuratu(object):

    def __init__(self):
        super(pasahitzaBerreskuratu, self).__init__()
        self.window = tk.Tk()
        self.window.title("Pasahitza berreskuratzeko orria")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'


        self.Erregistroa = tk.Label(self.window, text="PASAHITZA BERRESKURATZEKO ORRIA", bg='CadetBlue1',
                               font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.erabiltzaileaL = tk.Label(self.window, text="Erabiltzailea:", bg='CadetBlue1', font=("Times", 11))
        self.erabiltzaileaL.place(x=80, y=70)

        self. erabiltzaileaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, validate="key")
        self.erabiltzaileaE.pack(pady=5, padx=5, ipadx=20)

        gakoGalderaL = tk.Label(self.window, text="Berreskurapen-galdera:", bg='CadetBlue1', font=("Times", 11))
        gakoGalderaL.place(x=75, y=100)

        self.gakoGalderaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.gakoGalderaE.pack(pady=5, padx=5, ipadx=20)

        self.gakoaL = tk.Label(self.window, text="Berreskurapen-gakoa:", bg='CadetBlue1', font=("Times", 11))
        self.gakoaL.place(x=75, y=130)

        self.gakoaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL)
        self.gakoaE.pack(pady=5, padx=5, ipadx=20)

        self.pasahitzaBerriaL = tk.Label(self.window, text="Pasahitz berria:", bg='CadetBlue1', font=("Times", 11))
        self.pasahitzaBerriaL.place(x=80, y=160)

        self.pasahitzaBerriaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, show="•")
        self.pasahitzaBerriaE.pack(pady=5, padx=5, ipadx=20)

        tk.Button(
            self.window,
            text="Pasahitza aldatu",
            padx=10,
            pady=5,
            bg="AliceBlue",
            command=self.printValue
        ).pack(pady=20)


        tk.Button(self.window, text="Itzuli", padx=10, pady=5, bg="AliceBlue", command=self.atzera).pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def atzera(self):
        self.window.destroy()
        view.ongietorrileioa.ongietorrileioa().__init__()




    def printValue(self):
        erabiltzailea=self.erabiltzaileaE.get()
        gakoa=self.gakoaE.get()
        gakoGaldera=self.gakoGalderaE.get()
        pasahitzaBerria=self.pasahitzaBerriaE.get()


        if ((len(erabiltzailea)!=0) &(len(gakoa)!=0 )&(len(pasahitzaBerria)!=0 ) &(len(gakoGaldera)!=0 )):
            #begiratu erabiltzaile eta pasahitz egokia sortu dituen
            #dago=Konexioa.gakoakKonprobatu(Konexioa(),erabiltzailea,gakoGaldera,gakoa)
            erab=Jokalariak().getErabiltzaileaInfo(erabiltzailea)
            print(erab.gakoGaldera)

            if (erab.gakoGaldera==gakoGaldera and erab.gakoa==gakoa):
                # update
                erab.pasahitzaAldatu(pasahitzaBerria)
                #Konexioa.pasahitzaAldatu(Konexioa(),erabiltzailea,pasahitzaBerria)
                self.window.destroy()
                view.saioaHasi.saioaHasi().__init__()

            else:
                tk.Label(self.window, text='Sartutako informazioa ez da egokia, saiatu berriz mesedez.', pady=10,
                         padx=90, bg='CadetBlue1',
                         font=("Times", 14, "bold")).place(relx=.5, rely=.9, anchor=CENTER)

        else:
            tk.Label(self.window, text='Bete itzazu eremu guztiak mesedez.', pady=10,padx=100, bg='CadetBlue1',font=("Times", 14, "bold")).place(relx=.5, rely=.9,anchor= CENTER)

