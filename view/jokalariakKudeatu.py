import tkinter as tk
from view.JokatuLeioa import JokatuLeioa

class jokalariakKudeatu(object):


    def __init__(self):
        super(jokalariakKudeatu,self).__init__()
        self.window = tk.Tk()
        self.window.title("Jokalariak kudeatzeko menua")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="Hauek dira jokalariak", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)


        self.window.mainloop()





