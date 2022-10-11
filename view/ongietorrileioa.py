import tkinter as tk
from view.saioaHasi import saioaHasi
from view.erregistratu import erregistratu
from view.pasahitzaAldatu import pasahitzaAldatu
from view.pasahitzaBerreskuratu import pasahitzaBerreskuratu

class ongietorrileioa(object):


    def __init__(self):
        super(ongietorrileioa,self).__init__()
        self.window = tk.Tk()
        self.window.title("Ongi Etorri!")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="ONGI ETORRI!", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="Hasi saioa",padx=40,pady=5, command=self.saioaHasi)
        button.pack(pady=10)
        button1 = tk.Button(self.window, text="Erregistratu",padx=40,pady=5,command=self.erregistratu)
        button1.pack(pady=10)
        button2 = tk.Button(self.window, text="Pasahitza berreskuratu",padx=10,pady=5,command=self.pasahitzaBerreskuratu)
        button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Pasahitza aldatu",padx=30,pady=5,command=self.pasahitzaAldatu)
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



