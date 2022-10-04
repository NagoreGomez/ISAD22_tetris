from view.JokatuLeioa import JokatuLeioa
from view.ongietorrileioa import ongietorrileioa
from view.erregistratu import erregistratu

import sqlite3

con = sqlite3.connect("datubasea.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Erabiltzaileak (erabiltzailea, IzenAbizenak, helbideElektronikoa, pasahitza)")
con.commit()


query="""INSERT INTO Erabiltzaileak  VALUES ('A', 'Nagore Gomez', 'a@gmail.com', 1111);"""
print(query)
cur.execute(query)
con.commit()

res = cur.execute("SELECT * FROM Erabiltzaileak")
print(res.fetchall())




if __name__ == '__main__':
	ongietorrileioa()
	tetris = JokatuLeioa()
	ongietorrileioa()
	erregistratu()