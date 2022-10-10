import tkinter as tk

class ongietorrileioa(object):


    def __init__(self):
        super(ongietorrileioa,self).__init__()
        self.window = tk.Tk()
        self.window.title("Ongi Etorri!")
        self.window.geometry('600x400')
        self.window['bg'] = 'CadetBlue1'

        self.Erregistroa = tk.Label(self.window, text="ONGI ETORRI!", bg='CadetBlue1', font=("Times", 14, "bold"))
        self.Erregistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

        button = tk.Button(self.window, text="Hasi saioa",padx=40,pady=5)
        button.pack(pady=10)
        button1 = tk.Button(self.window, text="Erregistratu",padx=40,pady=5)
        button1.pack(pady=10)
        button2 = tk.Button(self.window, text="Pasahitza berreskuratu",padx=10,pady=5)
        button2.pack(pady=10)
        button3 = tk.Button(self.window, text="Pasahitza aldatu",padx=30,pady=5)
        button3.pack(pady=10)

        self.window.mainloop()


