import tkinter as tk

class ongietorrileioa(object):


    def __init__(self):
        super(ongietorrileioa,self).__init__()
        self.window = tk.Tk()
        self.window.geometry('600x400')
        #self.window.attributes('-fullscreen',True)
        self.window.title("Ongi Etorri")
        button = tk.Button(self.window, text="Hasi saioa")
        button.pack()
        button1 = tk.Button(self.window, text="Erregistratu")
        button1.pack()
        button2 = tk.Button(self.window, text="Pasahitza berreskuratu")
        button2.pack()
        button3 = tk.Button(self.window, text="Pasahitza aldatu")
        button3.pack()

        self.window.mainloop()


