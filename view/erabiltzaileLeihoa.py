import sys
import tkinter as tk
from view.abiadurak import abiadurak
import view
from view.pertsonalizatu import pertsonalizatu

class erabiltzaileLeihoa(object):

    def __init__(self):
        super(erabiltzaileLeihoa,self).__init__()
        self.window = tk.Tk()
        self.window.title("Erabiltzaile menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="ERABILTZAILEAREN ORRIA", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="Jolastu",padx=40,pady=5,command=self.jokatu)
        button.pack(pady=10)
        button3 = tk.Button(self.window, text="Partida pertsonalizatu", padx=40, pady=5, command=self.pertsonalizazioa)
        button3.pack(pady=10)
        button2 = tk.Button(self.window,text="Itzuli",padx=40,pady=5,command=self.itzuli)
        button2.pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def jokatu(self):
        self.window.destroy()
        view. abiadurak.abiadurak().__init__()


    def pertsonalizazioa(self):
        self.window.destroy()
        view.pertsonalizatu.pertsonalizatu()

    def itzuli(self):
        self.window.destroy()
        view.saioaHasi.saioaHasi()




