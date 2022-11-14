import sqlite3


class Konexioa(object):

    def __init__(self):
        super(Konexioa, self).__init__()
        self.con=sqlite3.connect("datubasea.db")
        self.cur = self.con.cursor()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Erabiltzaileak(erabiltzailea, izenAbizenak, helbideElektronikoa, pasahitza,gakoGaldera,gakoa,fondoa,adreiluak,soinua)")

        res = self.cur.execute("SELECT * FROM Erabiltzaileak WHERE erabiltzailea='admin'")

        if res.fetchone() is None:
            self.cur.execute("INSERT INTO Erabiltzaileak VALUES ('admin','admin','admin@gmail.com','123','admin?','bai','a','a','a')")
            self.con.commit()

    def erabiltzailearenPasahitza (self,erabiltzailea):
        res = self.cur.execute("SELECT pasahitza FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        pas = res.fetchone()
        if pas is None:
            return pas
            print(pas)
        else:
            return pas[0]
            print(pas[0])


    def erabiltzaileaKonprobatu(self,erabiltzailea):
        res = self.cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        erab = res.fetchone()
        if erab is None:
            return erab
        else:
            return erab[0]


    def erabiltzaileaGehitu(self,izena,erabiltzailea,email,pasahitza,gakoa,gakoGaldera):
        self.cur.execute("INSERT INTO Erabiltzaileak VALUES(?, ?, ?,?,?,?)",
                    (erabiltzailea, izena, email, pasahitza, gakoGaldera, gakoa))
        self.con.commit()


    def konexioa_itxi(self):
        self.con.close()


    def pertsonalizazioaGorde(self,kolorea,adreiluak,soinua,erabiltzailea):
        self.cur.execute("UPDATE Erabiltzaileak SET fondoa=(?), adreiluak=(?), soinua=(?) WHERE erabiltzailea=(?)",  (kolorea,adreiluak,soinua,erabiltzailea))
        self.con.commit()


    def getAtzekoKolorea(self,erabiltzailea):
        res=self.cur.execute("SELECT fondoa FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        fondoa = res.fetchone()
        return fondoa[0]

    def getAdreiluak(self,erabiltzailea):
        res=self.cur.execute("SELECT adreiluak FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        adreiluak = res.fetchone()
        return adreiluak[0]
