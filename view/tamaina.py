import tkinter as tk
from view.JokatuLeioa import JokatuLeioa
from view.abiadura import abiadura

class ongietorrileioa(object):


    def __init__(self):
        super(ongietorrileioa,self).__init__()
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

    def saioaHasi(self):
        self.window.destroy()
        saioaHasi().__init__()

    def erregistratu(self):
        self.window.destroy()
        erregistratu().__init__()
    def pasahitzaBerreskuratu(self):
        self.window.destroy()
        pasahitzaBerreskuratu().__init__()
    def pasahitzaAldatu(self):
        self.window.destroy()
        pasahitzaAldatu().__init__()



