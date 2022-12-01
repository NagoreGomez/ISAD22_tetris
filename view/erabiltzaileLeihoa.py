import sys
import tkinter as tk

import pygame


from view.abiadurak import abiadurak
import view
from view.pertsonalizatu import pertsonalizatu
from controller.konexioa import Konexioa
from view.jokalariakKudeatu import jokalariakKudeatu
from view.RankingHautatu import RankigHautatu

class erabiltzaileLeihoa(object):

    def __init__(self,erabiltzailea):
        super(erabiltzaileLeihoa,self).__init__()
        self.erabiltzailea=erabiltzailea
        self.window = tk.Tk()
        self.window.title(" Menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'


        self.Erregistroa = tk.Label(self.window, text="ERABILTZAILEAREN ORRIA", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="Jolastu",padx=40,pady=5,command=self.jokatu)
        button.pack(pady=10)
        button3 = tk.Button(self.window, text="Partida pertsonalizatu", padx=40, pady=5, command=self.pertsonalizazioa)
        button3.pack(pady=10)



        erab=Konexioa.erabiltzaileaKonprobatu(Konexioa(),erabiltzailea)
        if (erab=='admin'):
            button1 = tk.Button(self.window, text="Jokalariak kudeatu", padx=40, pady=5, command=self.administratu)
            button1.pack(pady=10)





        self.partida=Konexioa.partidaKargatu(Konexioa(), self.erabiltzailea)

        if (self.partida != "#"):
            button4 = tk.Button(self.window, text="Gordetako partida berreskuratu", padx=40, pady=5,
                                command=self.partidaKargatu)
            button4.pack(pady=10)
        # ASI O QUE NO APAREZCA?????
        else:
            button4 = tk.Button(self.window, text="Gordetako partida berreskuratu", padx=40, pady=5, state="disabled")
            button4.pack(pady=10)

        button = tk.Button(self.window, text="Ranking-ak ikusi", padx=40, pady=5, command=self.rankingaikusi)
        button.pack(pady=10)

        button2 = tk.Button(self.window,text="Itzuli",padx=40,pady=5,command=self.itzuli)
        button2.pack(pady=10)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()

    def administratu(self):
        self.window.destroy()
        view.jokalariakKudeatu.jokalariakKudeatu(self.erabiltzailea).__init__()
    def rankingaikusi(self):
        self.window.destroy()
        view.RankingHautatu.RankigHautatu(self.erabiltzailea).__init__()


    def jokatu(self):
        self.window.destroy()
        view.abiadurak.abiadurak(self.erabiltzailea).__init__()

    def pertsonalizazioa(self):
        self.window.destroy()
        view.pertsonalizatu.pertsonalizatu(self.erabiltzailea)

    def itzuli(self):
        self.window.destroy()
        view.saioaHasi.saioaHasi()

    def partidaKargatu(self):
        self.window.destroy()
        datuak = str(self.partida).split(sep='/')
        puntuak = int(datuak[0])
        tamainax = int(datuak[1])
        tamainay=int(datuak[2])
        abiadura = int(datuak[3])

        view.JokatuLeihoa.JokatuLeihoa(abiadura, tamainax, tamainay, self.erabiltzailea, puntuak, self.partida).__init__()





