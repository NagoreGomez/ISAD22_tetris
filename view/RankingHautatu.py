import sqlite3
import sys
import tkinter as tk
from tkinter import *
import view
from controller.konexioa import Konexioa
from view.rankingAbsolutua import RankingAbsolutua
from view.rankingX import RankingX


class RankigHautatu(object):
    def __init__(self,erabiltzailea):
        super(RankigHautatu,self).__init__()
        self.erabiltzailea=erabiltzailea
        self.window = tk.Tk()
        self.window.title("Pertsonalizazio menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'


        self.aukeraabsolutua = tk.StringVar()
        self.aukeraabsolutua.set(value="0")

        self.RankigHautatu = tk.Label(self.window, text="RANKIG-A HAUTATU", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.RankigHautatu.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.absolutua = tk.Label(self.window, text="RANKING ABSOLUTUA:", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.absolutua.place(x=100, y=70)

        self.absolutua1 = tk.Radiobutton(self.window,variable=self.aukeraabsolutua,value=1, bg='CadetBlue1', font=("Times", 12))
        self.absolutua1.place(x=300, y=70)




        self.aukeraabiadura = tk.StringVar()
        self.aukeraabiadura.set(value="0")

        self.mailako = tk.Label(self.window, text="MAILAKO RANKIG-AK", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.mailako.place(x=100, y=100)

        self.abiadura = tk.Label(self.window, text="Abiadura:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.abiadura.place(x=100, y=140)

        self.abiadura1 = tk.Radiobutton(self.window,variable=self.aukeraabiadura, text="Motela", value=1, bg='CadetBlue1', font=("Times", 12),tristatevalue="x")
        self.abiadura1.place(x=100, y=170)

        self.abiadura2 = tk.Radiobutton(self.window,variable=self.aukeraabiadura, text="Ertaina",value=2, bg='CadetBlue1', font=("Times", 12),tristatevalue="x")
        self.abiadura2.place(x=200, y=170)

        self.abiadura3 = tk.Radiobutton(self.window,variable=self.aukeraabiadura, text="Azkarra",value=3, bg='CadetBlue1', font=("Times", 12))
        self.abiadura3.place(x=300, y=170)

        self.aukeratamaina = tk.StringVar()
        self.aukeratamaina.set(value="0")



        self.tamaina = tk.Label(self.window, text="Tamaina:", bg='CadetBlue1', font=("Times", 12,"bold"))
        self.tamaina.place(x=100, y=200)

        self.tamaina1 = tk.Radiobutton(self.window,variable=self.aukeratamaina, text="10x20", value=1, bg='CadetBlue1', font=("Times", 12))
        self.tamaina1.place(x=100, y=230)

        self.tamaina2 = tk.Radiobutton(self.window,variable=self.aukeratamaina, text="15x25", value=2, bg='CadetBlue1', font=("Times", 12))
        self.tamaina2.place(x=200, y=230)

        self.tamaina3 = tk.Radiobutton(self.window,variable=self.aukeratamaina, text="20x30", value=3, bg='CadetBlue1', font=("Times", 12))
        self.tamaina3.place(x=300, y=230)

        button2 = tk.Button(self.window, text="Ikusi", padx=30, pady=5, command=self.pertsonalizazioa)
        button2.place(x=110, y=300)

        button3 = tk.Button(self.window, text="Itzuli", padx=40, pady=5, command=self.itzuli)
        button3.place(x=310, y=300)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)

        self.window.mainloop()

    def itzuli(self):
        self.window.destroy()
        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea).__init__()

    def pertsonalizazioa(self):

        self.absolutua = "0"
        self.abiadura = "0"
        self.tamaina = "0"




        if ((self.aukeraabsolutua.get() == "1" ) and self.aukeraabiadura.get()!="1" and self.aukeraabiadura.get()!="2" and self.aukeraabiadura.get()!="3" and self.aukeratamaina.get()!="1" and self.aukeratamaina.get()!="2" and self.aukeratamaina.get()!="2"): #solo absoluto selecionado
            self.absolutua = "1"


        elif((self.aukeraabsolutua.get() == "0" ) and (self.aukeraabiadura.get()!="0") and (self.aukeratamaina.get()!="0" )): #solo abiadura y tamaina selecionado

            if (self.aukeraabiadura.get() == "1"):
                self.abiadura = "1"
            elif (self.aukeraabiadura.get() == "2"):
                self.abiadura = "2"
            elif (self.aukeraabiadura.get() == "3"):
                self.abiadura = "3"


            if (self.aukeratamaina.get() == "1"):
                self.tamaina = "1"
            elif (self.aukeratamaina.get() == "2"):
                self.tamaina = "2"
            elif (self.aukeratamaina.get() == "3"):
                self.tamaina = "3"

        else: #cualquier otra convinacion
            tk.Label(self.window, text='Aukera ez da egokia, saiatu berriz.', pady=10,
                     padx=90, bg='CadetBlue1',
                     font=("Times", 14, "bold")).place(relx=.5, rely=.7, anchor=CENTER)


        print(self.absolutua)
        print(self.abiadura)
        print(self.tamaina)

        if(self.absolutua=="1"):
            self.window.destroy()
            view.rankingAbsolutua.RankingAbsolutua(self.erabiltzailea).__init__()
        else:
            self.window.destroy()
            view.rankingX.RankingX(self.erabiltzailea,self.tamaina,self.abiadura).__init__()



