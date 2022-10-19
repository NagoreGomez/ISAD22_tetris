import sqlite3
import tkinter as tk

import view.administratzaileLeihoa
#from view.JokatuLeioa import JokatuLeioa
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

        self.aukera = tk.StringVar()
        self.aukera.set(value="")
        con = sqlite3.connect("datubasea.db")
        cur = con.cursor()
        cur.execute("SELECT erabiltzailea FROM Erabiltzaileak")
        res = cur.fetchall()
        self.i=0
        for row in res:
            #self.l=tk.Label(self.window,text=row)
            #self.l.pack(pady=5)
            tk.Radiobutton(self.window, text=row, variable=self.aukera, value=row).pack(pady=5)
            #self.i=self.i+1

        button2 = tk.Button(self.window,text="Ezabatu",padx=40,pady=5,command=self.ezabatu)
        button2.pack()

        button3 = tk.Button(self.window,text="Itzuli",padx=40,pady=5,command=self.atzera)
        button3.pack()


        self.window.mainloop()

    def ezabatu(self):
        erab = self.aukera.get()
        con = sqlite3.connect("datubasea.db")
        cur = con.cursor()
        res = cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?)",(erab,))
        ezDago = res.fetchone() is None
        if(ezDago):
            print(-1)
        else:
            tk.Label(self.window, text=f'{erab}, Bai dago datu basean eta ezabatuko da!', pady=10, padx=180,
                     font=("Times", 14, "bold"),
                     bg='CadetBlue1').pack()
            cur.execute("DELETE FROM Erabiltzaileak WHERE erabiltzailea=(?)",(erab,))
            con.commit()
        #self.window.destroy()
        #ezabatuErabiltzaile()

    #def hartuJokalariak(self):


    def atzera(self):
        self.window.destroy()
        view.administratzaileLeihoa.administratzaileLeihoa()