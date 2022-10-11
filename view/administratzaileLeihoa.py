import tkinter as tk
from view.JokatuLeioa import JokatuLeioa
from view.jokalariakKudeatu import jokalariakKudeatu

class administratzaileLeihoa(object):


    def __init__(self):
        super(administratzaileLeihoa,self).__init__()
        self.window = tk.Tk()
        self.window.title("Administratzaile menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="Zer egin nahi duzu?", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="Jolastu",padx=40,pady=5,command=self.jokatu)
        button.pack(pady=10)
        button1 = tk.Button(self.window, text="Admistratzaileak kudeatu",padx=40,pady=5, command=self.administratu)
        button1.pack(pady=10)


        self.window.mainloop()

    def jokatu(self):
        self.window.destroy()
        JokatuLeioa().__init__()

    def administratu(self):
        self.window.destroy()
        jokalariakKudeatu().__init__()


