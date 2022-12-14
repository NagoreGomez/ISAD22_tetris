import sys
import tkinter as tk
from tkinter import *



class saria(object):

    def __init__(self,erabiltzailea,tamainax,tamainay,abiadura,puntuak, partidaKop):
        super(saria, self).__init__()
        self.window = tk.Tk()
        self.window.title("Saria")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        if(abiadura==800):
            abiaduraMota='motelean'
        elif(abiadura==400):
            abiaduraMota='ertainean'
        elif (abiadura ==100):
            abiaduraMota = 'azkarrean'


        Erregistroa = tk.Label(self.window, text="ZORIONAK!", bg='CadetBlue1', font=("Times", 24, "bold"))
        Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        self.saria = tk.Label(self.window, text=f'{erabiltzailea}, sari bat irabazi duzu:', bg='CadetBlue1', font=("Times", 14))
        self.saria.pack(pady=10, padx=5, ipadx=10, ipady=10)

        self.info = tk.Label(self.window,
                              text=f'{tamainax}x{tamainay} tamainan eta abiadura {abiaduraMota}, {partidaKop} partida jolasteagatik {puntuak} puntura.',
                              bg='CadetBlue1', font=("Times", 14))
        self.info.pack(pady=10, padx=5, ipadx=10, ipady=10)

        #irudia=PhotoImage(file="/irudiak/celebracion.jpg")
        #Label(self.window,image=irudia).place(x=100,y=100);




        self.window.mainloop()



