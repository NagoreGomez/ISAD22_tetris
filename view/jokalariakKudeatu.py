import sqlite3
import tkinter as tk

import view.administratzaileLeihoa
from view.JokatuLeioa import JokatuLeioa
from view.ezabatuErabiltzaile import ezabatuErabiltzaile

class jokalariakKudeatu(object):


    def __init__(self):
        super(jokalariakKudeatu,self).__init__()
        self.window = tk.Tk()
        self.window.title("Jokalariak kudeatzeko menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="Hauek dira jokalariak", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.hartuJokalariak()

        button2 = tk.Button(self.window,text="Ezabatu",padx=40,pady=5,command=self.ezabatu)
        button2.pack()

        button3 = tk.Button(self.window,text="Atzera",padx=40,pady=5,command=self.atzera)
        button3.pack()
        self.window.mainloop()

    def ezabatu(self):
        self.window.destroy()
        ezabatuErabiltzaile()

    def hartuJokalariak(self):
        con = sqlite3.connect("datubasea.db")
        cur = con.cursor()
        cur.execute("SELECT erabiltzailea FROM Erabiltzaileak")
        res = cur.fetchall()
        for row in res:
            self.l=tk.Label(self.window,text=row)
            self.l.pack(pady=5)
            print("\n")

    def atzera(self):
        self.window.destroy()
        view.administratzaileLeihoa.administratzaileLeihoa()