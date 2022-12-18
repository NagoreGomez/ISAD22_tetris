import sys
import tkinter as tk
import view.erabiltzaileLeihoa
from model.Ranking import Ranking


class RankingAbsolutua(object):


    def __init__(self,erabiltzailea):
        super(RankingAbsolutua,self).__init__()
        self.window = tk.Tk()
        self.erabiltzailea=erabiltzailea
        self.window.title("Ranking")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'



        self.Erregistroa = tk.Label(self.window, text="RANKING-A IKUSTEKO ORRIA", bg='CadetBlue1',
                                    font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.aukera = tk.StringVar()
        self.aukera.set(value=" ")


        # taularen goiko aldea
        # taularen goiko aldea
        self.t1 = tk.Label(self.window, text="Posizioa", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t1.place(x=5, y=70)

        self.t1 = tk.Label(self.window, text="Erabiltzailea", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t1.place(x=100, y=70)

        self.t2 = tk.Label(self.window, text="Abiadura", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t2.place(x=220, y=70)

        self.t3 = tk.Label(self.window, text="Tamaina", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t3.place(x=320, y=70)

        self.t4 = tk.Label(self.window, text="Puntuak", bg='CadetBlue1', font=("Times", 12, "bold"))
        self.t4.place(x=420, y=70)

        i = 100
        pos=1
        #ranking=Konexioa.getRanking(Konexioa())
        ranking=Ranking().getRankingAbsolutua()
        luzera = len(ranking)


        unekoPos = 0
        while (unekoPos < luzera):

            erabiltzailea, tamaina, abiadura, puntuak = ranking[unekoPos]

            if(puntuak!=0):
                self.erab = tk.Label(self.window, text=pos, bg='CadetBlue1', font=("Times", 12))
                self.erab.place(x=20, y=i)

                self.erab = tk.Label(self.window, text=erabiltzailea, bg='CadetBlue1', font=("Times", 12))
                self.erab.place(x=120, y=i)

                self.tamaina = tk.Label(self.window, text=tamaina, bg='CadetBlue1', font=("Times", 12))
                self.tamaina.place(x=240, y=i)

                self.abiadura = tk.Label(self.window, text=abiadura, bg='CadetBlue1', font=("Times", 12))
                self.abiadura.place(x=340, y=i)

                self.puntuak = tk.Label(self.window, text=puntuak, bg='CadetBlue1', font=("Times", 12))
                self.puntuak.place(x=440, y=i)
                i = i + 30
                pos=pos+1
            unekoPos = unekoPos + 1


        button3 = tk.Button(self.window,text="Itzuli",padx=40,pady=5,command=self.atzera)
        button3.place(x=200, y=i+80)

        # lehioa ondo ixteko
        self.window.protocol("WM_DELETE_WINDOW", sys.exit)
        self.window.mainloop()


    def atzera(self):
        self.window.destroy()
        view.RankingHautatu.RankigHautatu(self.erabiltzailea).__init__()
