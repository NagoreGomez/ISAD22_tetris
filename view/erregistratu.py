from tkinter import *
import tkinter as tk

import sqlite3

window = tk.Tk()
window.title("Erregistratzeko orria")
window.geometry('600x400')
window['bg'] = 'CadetBlue1'



def printValue():
    izena = izenaE.get()
    erabiltzailea=erabiltzaileaE.get()
    email=emailE.get()
    pasahitza=pasahitzaE.get()
    if ((len(izena)!=0 )&(len(erabiltzailea)!=0) &(len(email)!=0 )&(len(pasahitza)!=0 )):
        tk.Label(window, text=f'{izena}, erregistratu zara!', pady=10,padx=90, bg='CadetBlue1',font=("Times", 14, "bold")).place(relx=.5, rely=.7,anchor= CENTER)


        #insert




    else:
        tk.Label(window, text='Bete itzazu eremu guztiak mesedez.', pady=10, bg='CadetBlue1',font=("Times", 14, "bold")).place(relx=.5, rely=.7,anchor= CENTER)




Errgistroa = tk.Label(window, text="ERREGISTRATZEKO ORRIA", bg='CadetBlue1',font=("Times", 14, "bold"))
Errgistroa.pack(pady=10, padx=20, ipadx=10, ipady=10)

izenaL = tk.Label(window, text="Izena:", bg='CadetBlue1',font=("Times", 11))
izenaL.place(x=80, y=70)


izenaE = tk.Entry(window,justify=tk.LEFT, state=tk.NORMAL)
izenaE.pack(pady=5, padx=5, ipadx=20)

erabiltzaileaL = tk.Label(window, text="Erabiltzailea:", bg='CadetBlue1',font=("Times", 11))
erabiltzaileaL.place(x=80, y=100)

erabiltzaileaE = tk.Entry(window,justify=tk.LEFT, state=tk.NORMAL,validate="key")
erabiltzaileaE.pack(pady=5, padx=5,ipadx=20)

emailL = tk.Label(window, text="Helbide elektronikoa:", bg='CadetBlue1',font=("Times", 11))
emailL.place(x=80, y=130)

emailE = tk.Entry(window,justify=tk.LEFT, state=tk.NORMAL)
emailE.pack(pady=5, padx=5,ipadx=20)

pasahitzaL = tk.Label(window, text="Pasahitza:", bg='CadetBlue1',font=("Times", 11))
pasahitzaL.place(x=80, y=160)

pasahitzaE = tk.Entry(window,justify=tk.LEFT, state=tk.NORMAL,show="•")
pasahitzaE.pack(pady=5, padx=5,ipadx=20)


tk.Button(
    window,
    text="Erregistratu",
    padx=10,
    pady=5,
    bg="AliceBlue",
    command=printValue
    ).pack(pady=20)

window.mainloop()