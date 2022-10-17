import tkinter as tk

#from view.saioaHasi import saioaHasi
import view
#from view.saioaHasi import saioaHasi
#from view.erregistratu import erregistratu
#from view.pasahitzaAldatu import pasahitzaAldatu
#from view.pasahitzaBerreskuratu import pasahitzaBerreskuratu
from view.tamaina import tamaina
class abiadurak(object):


    def __init__(self):
        super(abiadurak,self).__init__()
        self.window = tk.Tk()
        self.window.title("Ongi Etorri!")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="ABIADURA HAUTATU", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="1. ABIADURA",padx=40,pady=5,command=self.tamaina)
        button.pack(pady=10)
        button1 = tk.Button(self.window, text="2. ABIADURA",padx=40,pady=5,command=self.tamaina)
        button1.pack(pady=10)
        button2 = tk.Button(self.window, text="3. ABIADURA",padx=10,pady=5,command=self.tamaina)
        button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Atzera",padx=30,pady=5,command=self.atzera)
        button3.pack(pady=10)

        self.window.mainloop()

    def tamaina(self):
        self.window.destroy()
        tamaina()

    def atzera(self):
        self.window.destroy()
        view.saioaHasi.saioaHasi().__init__()

