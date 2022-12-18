import sys
import tkinter as tk


import view
from view.tamaina import tamaina



class abiadurak(object):


    def __init__(self,erabiltzailea):
        super(abiadurak,self).__init__()
        self.erabiltzailea = erabiltzailea
        self.window = tk.Tk()
        self.window.title("Ongi Etorri!")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.aukera = tk.IntVar()
        self.aukera.set(value=1)


        self.Erregistroa = tk.Label(self.window, text="ABIADURA HAUTATU", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.button = tk.Radiobutton(self.window, text="MOTELA",padx=40,pady=5, variable=self.aukera, value=1)
        self.button.pack(pady=10)
        self.button1 = tk.Radiobutton(self.window, text="ERTAINA",padx=40,pady=5, variable=self.aukera, value=2)
        self.button1.pack(pady=10)
        self.button2 = tk.Radiobutton(self.window, text="AZKARRA",padx=40,pady=5, variable=self.aukera, value=3)
        self.button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Hautatu", padx=30, pady=5, command=self.tamaina)
        button3.pack(pady=10)
        button4 = tk.Button(self.window, text="Itzuli",padx=30,pady=5,command=self.itzuli)
        button4.pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def tamaina(self):
        abiadura=0
        self.window.destroy()
        if (self.aukera.get() == 1):
            abiadura = 800
        elif (self.aukera.get() == 2):
            abiadura = 400
        elif (self.aukera.get() == 3):
            abiadura = 100

        tamaina(abiadura,self.erabiltzailea).__init__()

    def itzuli(self):
        self.window.destroy()

        view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea).__init__()

