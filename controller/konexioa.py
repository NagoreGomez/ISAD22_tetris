import sqlite3


class konexioa(object):

    def __int__(self):
        super(konexioa, self).__int__()
        self.con=sqlite3.connect("datubasea.db")
        self.cur = self.con.cursor()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Erabiltzaileak(erabiltzailea, izenAbizenak, helbideElektronikoa, pasahitza,gakoGaldera,gakoa)")

        res = self.cur.execute("SELECT * FROM Erabiltzaileak WHERE erabiltzailea=admin")

        if res.fetchone() is None:
            self.cur.execute("INSERT INTO Erabiltzaileak VALUES ('admin','admin','admin@gmail.com','123','admin?','bai')")
            self.con.commit()

    def erabiltzailearenPasahitza(self,erabiltzailea):
        res = self.cur.execute("SELECT pasahitza FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        pas = res.fetchone()
        if pas is None:
            return pas
        else:
            return pas[0]



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
