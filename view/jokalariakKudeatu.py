import sqlite3
import sys
import tkinter as tk

from tkinter import *
from tkinter import ttk

import view.administratzaileLeihoa
#from view.JokatuLeioa import JokatuLeioa

class jokalariakKudeatu(object):


    def __init__(self):
        super(jokalariakKudeatu,self).__init__()
        self.window = tk.Tk()
        self.window.title("Jokalariak kudeatzeko menua")
        self.window.geometry('1000x400')
        self.window['bg'] = 'CadetBlue1'


        """
        #main frame
        main_frame= Frame(self.window)
        main_frame.pack(fill=BOTH, expand=1)
        #canvas
        my_canvas= Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        #scrollbar
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
         #confiure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        #another frame insside canvas
        second_frame= Frame(my_canvas)
        #add the new to a window in canvas
        my_canvas.create_window((0,0),window=second_frame,anchor="nw")

        """

        self.Erregistroa = tk.Label(self.window, text="Hauek dira jokalariak", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.aukera = tk.StringVar()
        self.aukera.set(value=" ")
        con = sqlite3.connect("datubasea.db")
        cur = con.cursor()

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
        cur.execute("SELECT erabiltzailea FROM Erabiltzaileak")
        res = cur.fetchall()
        i = 100
        for row in res:
            self.botoia = tk.Radiobutton(self.window, variable=self.aukera, value=row, bg='CadetBlue1',font=("Times", 12))
            self.botoia.place(x=900, y=i)
            i = i + 30

            # self.i=self.i+1


        #erabiltzailea
        cur.execute("SELECT erabiltzailea FROM Erabiltzaileak")
        res = cur.fetchall()
        i = 100
        for row in res:
            #self.l=tk.Label(self.window,text=row)
            #self.l.pack(pady=5)
            self.erab=tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.erab.place(x=10, y=i)
            i=i+30
            #self.i=self.i+1


        #izena
        cur.execute("SELECT izenAbizenak FROM Erabiltzaileak")
        res = cur.fetchall()
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=150, y=i)
            i = i + 30

        # email
        cur.execute("SELECT helbideElektronikoa FROM Erabiltzaileak")
        res = cur.fetchall()
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=300, y=i)
            i = i + 30

        # pasahitza
        cur.execute("SELECT pasahitza FROM Erabiltzaileak")
        res = cur.fetchall()
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=500, y=i)
            i = i + 30

        # galko galdera
        cur.execute("SELECT gakoGaldera FROM Erabiltzaileak")
        res = cur.fetchall()
        i = 100
        for row in res:
            self.datuak = tk.Label(self.window, text=row, bg='CadetBlue1', font=("Times", 12))
            self.datuak.place(x=600, y=i)
            i = i + 30

        # gakoa
        cur.execute("SELECT gakoa FROM Erabiltzaileak")
        res = cur.fetchall()
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
        con = sqlite3.connect("datubasea.db")
        cur = con.cursor()
        res = cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?)",(erab,))
        ezDago = res.fetchone() is None
        if(ezDago):
            print(-1)
        else:
            cur.execute("DELETE FROM Erabiltzaileak WHERE erabiltzailea=(?)",(erab,))
            con.commit()
            self.window.destroy()
            jokalariakKudeatu().__init__()
        #self.window.destroy()
        #ezabatuErabiltzaile()

    #def hartuJokalariak(self):


    def atzera(self):
        self.window.destroy()
        view.administratzaileLeihoa.administratzaileLeihoa()