import sys
import tkinter as tk
from tkinter import *
import view
import sqlite3



class ezabatuErabiltzaile(object):

    def __init__(self):
        super(ezabatuErabiltzaile, self).__init__()
        self.window = tk.Tk()
        self.window.title("Ezabatzeko orria")
        self.window.geometry('600x500')
        self.window['bg'] = 'CadetBlue1'

        self.erabiltzaileaL = tk.Label(self.window, text="Erabiltzailea:",bg='CadetBlue1', font=("Times", 11))
        self.erabiltzaileaL.place(x=80,y=10)

        self.erabiltzaileaE = tk.Entry(self.window, justify=tk.LEFT, state=tk.NORMAL, validate="key")
        self.erabiltzaileaE.pack(pady=5, padx=5, ipadx=20)

        ezabatu = tk.Button(self.window,text="Ezabatu",padx=10,pady=5,bg="AliceBlue",command=self.ezabatu).pack(pady=15)

        atzera = tk.Button(self.window, text="Itzuli", padx=10, pady=5, bg="AliceBlue", command=self.itzuli).pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def itzuli(self):
        self.window.destroy()
        view.jokalariakKudeatu.jokalariakKudeatu()


    def ezabatu(self):
        erabiltzailea=self.erabiltzaileaE.get()
        con = sqlite3.connect("datubasea.db")
        cur = con.cursor()
        res = cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        ezDago = res.fetchone() is None

        if(ezDago):
            tk.Label(self.window, text='Ez dago datu basean erabitlzaile hori', pady=10, padx=180,
                     font=("Times", 14, "bold"),
                     bg='CadetBlue1').place(relx=.5, rely=.8, anchor=CENTER)
            print("Ez dago")

        else:
            tk.Label(self.window, text=f'{erabiltzailea}, Bai dago datu basean eta ezabatuko da!', pady=10, padx=180,
                     font=("Times", 14, "bold"),
                     bg='CadetBlue1').place(relx=.5, rely=.8, anchor=CENTER)

            cur.execute("DELETE FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
            con.commit()



