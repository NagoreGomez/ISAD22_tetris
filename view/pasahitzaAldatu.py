import sys
from tkinter import *
import tkinter as tk
import view
from model.Jokalariak import Jokalariak
from model.Jokalaria import Jokalaria

class pasahitzaAldatu(object):

    def __init__(self):
        super(pasahitzaAldatu, self).__init__()
        self.window = tk.Tk()
        self.window.title("Pasahitza aldatzeko orria")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'



        self.Erregistroa = tk.Label(self.window, text="PASAHITZA ALDATZEKO ORRIA", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.erabiltzaileaL = tk.Label(self.window, text="Erabiltzailea:", bg='CadetBlue1', font=("Times", 11))
        self.erabiltzaileaL.place(x=80, y=70)

        self.erabiltzaileaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, validate="key")
        self.erabiltzaileaE.pack(pady=5, padx=5, ipadx=20)

        self.pasahitzaL = tk.Label(self.window, text="Pasahitza:", bg='CadetBlue1', font=("Times", 11))
        self.pasahitzaL.place(x=80, y=100)

        self.pasahitzaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, show="•")
        self.pasahitzaE.pack(pady=5, padx=5, ipadx=20)

        self.pasahitzaBerriaL = tk.Label(self.window, text="Pasahitz berria:", bg='CadetBlue1', font=("Times", 11))
        self.pasahitzaBerriaL.place(x=80, y=130)

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

        # atzera
        tk.Button(self.window, text="Itzuli", padx=10, pady=5, bg="AliceBlue", command=self.atzera).pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def atzera(self):
        self.window.destroy()
        view.ongietorrileioa.ongietorrileioa().__init__()


    def printValue(self):

        erabiltzailea=self.erabiltzaileaE.get()
        pasahitza=self.pasahitzaE.get()
        pasahitzaBerria=self.pasahitzaBerriaE.get()


        if ((len(erabiltzailea) != 0) & (len(pasahitza) != 0) & (len(pasahitzaBerria) != 0)):
            # begiratu erabiltzaile eta pasahitz egokia sortu dituen
            #dago=Konexioa.erabiltzaileaEtaPasahitzaKonprobatu(Konexioa(),erabiltzailea,pasahitza)
            erab=Jokalariak().getErabiltzaileaInfo(erabiltzailea)
            if erab is not None:
                # update
                #Jokalaria().pasahitzaAldatu(erabiltzailea,pasahitzaBerria)
                erab.pasahitzaAldatu(pasahitzaBerria)
                #Konexioa.pasahitzaAldatu(Konexioa(),erabiltzailea,pasahitzaBerria)
                self.window.destroy()
                view.saioaHasi.saioaHasi().__init__()
            else:
                tk.Label(self.window, text='Sartutako informazioa ez da egokia, saiatu berriz mesedez.', pady=10,
                         padx=90, bg='CadetBlue1',
                         font=("Times", 14, "bold")).place(relx=.5, rely=.8, anchor=CENTER)

        else:
            tk.Label(self.window, text='Bete itzazu eremu guztiak mesedez.', pady=10, padx=100, bg='CadetBlue1',
                     font=("Times", 14, "bold")).place(relx=.5, rely=.8, anchor=CENTER)
