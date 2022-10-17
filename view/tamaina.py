import tkinter as tk

import view.JokatuLeioa
from view.JokatuLeioa import JokatuLeioa
#from view.abiadura import abiadura

class tamaina(object):


    def __init__(self):
        super(tamaina,self).__init__()
        self.window = tk.Tk()
        self.window.title("Ongi Etorri!")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="TAMAINA HAUTATU", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="10x20 TAMAINA ",padx=40,pady=5, command=self.JokatuLeioa)
        button.pack(pady=10)
        button1 = tk.Button(self.window, text="15x25 TAMAINA",padx=40,pady=5,command=self.JokatuLeioa)
        button1.pack(pady=10)
        button2 = tk.Button(self.window, text="20x30 TAMAINA",padx=10,pady=5,command=self.JokatuLeioa)
        button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Atzera",padx=30,pady=5,command=self.abiadura)
        button3.pack(pady=10)

        self.window.mainloop()

    def JokatuLeioa(self):
        self.window.destroy()
        JokatuLeioa()

    def abiadura(self):
        self.window.destroy()
        view.saioaHasi.abiadurak().__init__()

