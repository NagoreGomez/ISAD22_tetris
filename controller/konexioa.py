import sqlite3


class Konexioa(object):

    def __init__(self):
        super(Konexioa, self).__init__()
        self.con=sqlite3.connect("datubasea.db")
        self.cur = self.con.cursor()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Erabiltzaileak(erabiltzailea, izenAbizenak, helbideElektronikoa, pasahitza,gakoGaldera,gakoa,fondoa,adreiluak,soinua, puntuak, partida)")

        res = self.cur.execute("SELECT * FROM Erabiltzaileak WHERE erabiltzailea='admin'")

        if res.fetchone() is None:
            self.cur.execute("INSERT INTO Erabiltzaileak VALUES ('admin','admin','admin@gmail.com','123','admin?','bai','#98F5FF','1','soinua1', '0', '/')")
            self.con.commit()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS ErabiltzailePuntuazioa(erabiltzailea,abiadura,tamaina,puntuKop)")

        res = self.cur.execute("SELECT * FROM ErabiltzailePuntuazioa  WHERE erabiltzailea='admin'")

        if res.fetchone() is None:
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','1','1',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','1','2',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','1','3',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','2','1',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','2','2',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','2','3',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','3','1',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','3','2',0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','3','3',0)")



        #sariakkk
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Sariak(abiadura,tamaina,puntuKop,partidaKop)")

        res = self.cur.execute("SELECT * FROM Sariak")

        if res.fetchone() is None:
            self.cur.execute("INSERT INTO Sariak VALUES ('1','1','3000','2')")

            self.cur.execute("INSERT INTO Sariak VALUES ('1','2','3000','4')")

            self.cur.execute("INSERT INTO Sariak VALUES ('1','3','3000','6')")

            self.cur.execute("INSERT INTO Sariak VALUES ('2','1','1000','2')")

            self.cur.execute("INSERT INTO Sariak VALUES ('2','2','1000','4')")

            self.cur.execute("INSERT INTO Sariak VALUES ('2','3','1000','6')")

            self.cur.execute("INSERT INTO Sariak VALUES ('3','1','100','2')")

            self.cur.execute("INSERT INTO Sariak VALUES ('3','2','100','4')")

            self.cur.execute("INSERT INTO Sariak VALUES ('3','3','100','6')")

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


    def erabiltzaileaGehitu(self,izena,erabiltzailea,email,pasahitza,gakoa,gakoGaldera,fondoa,adreiluak,soinua,puntuak, partida):
        self.cur.execute("INSERT INTO Erabiltzaileak VALUES(?, ?, ?,?,?,?,?,?,?,?,?)",
                    (erabiltzailea, izena, email, pasahitza, gakoGaldera, gakoa,fondoa,adreiluak,soinua,puntuak, partida))

        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)",(erabiltzailea, '1','1','0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '1', '2', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '1', '3', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '2', '1', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '2', '2', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '2', '3', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '3', '1', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '3', '2', '0'))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?)", (erabiltzailea, '3', '3', '0'))

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

    def getSoinuak(self,erabiltzailea):
        res=self.cur.execute("SELECT soinua FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        soinua = res.fetchone()
        return soinua[0]

    def partidaGorde(self,erabiltzailea, partida, puntuak):
        self.cur.execute("UPDATE Erabiltzaileak SET partida=(?), puntuak=(?) WHERE erabiltzailea=(?)",
                         (partida, puntuak, erabiltzailea))
        self.con.commit()

    def partidaKargatu(self,erabiltzailea):
        res=self.cur.execute("SELECT partida FROM Erabiltzaileak WHERE erabiltzailea=(?)",
                         (erabiltzailea,))
        partida=res.fetchone()
        return partida[0]

    def puntuakLortu(self, erabiltzailea):
        res = self.cur.execute("SELECT puntuak FROM Erabiltzaileak WHERE erabiltzailea=(?)",
                               (erabiltzailea,))
        puntuak = res.fetchone()
        return puntuak[0]

    def erabiltzaileaEtaPasahitzaKonprobatu(self,erabiltzailea,pasahitza):
        res = self.cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?) AND pasahitza=(?)", (erabiltzailea,pasahitza))
        erab = res.fetchone()
        if erab is None:
            return erab
        else:
            return erab[0]

    def pasahitzaAldatu(self,erabiltzailea,pasahitza):
        self.cur.execute("UPDATE Erabiltzaileak SET pasahitza=(?) WHERE erabiltzailea=(?)",(pasahitza, erabiltzailea))
        self.con.commit()


    def gakoakKonprobatu(self,erabiltzailea,gakoGaldera,gakoa):
        res = self.cur.execute("SELECT erabiltzailea FROM Erabiltzaileak WHERE erabiltzailea=(?) AND gakoa=(?) AND gakoGaldera=(?)",
                               (erabiltzailea, gakoa,gakoGaldera))
        egokia = res.fetchone()
        if egokia is None:
            return egokia
        else:
            return egokia[0]


    def getErabiltzailea(self):
        res = self.cur.execute("SELECT erabiltzailea FROM Erabiltzaileak")
        ema = res.fetchall()
        return ema

    def getIzena(self):
        res = self.cur.execute("SELECT izenAbizenak FROM Erabiltzaileak")
        ema = res.fetchall()
        return ema

    def getEmail(self):
        res = self.cur.execute("SELECT helbideElektronikoa FROM Erabiltzaileak")
        ema = res.fetchall()
        return ema

    def getPasahitza(self):
        res = self.cur.execute("SELECT pasahitza FROM Erabiltzaileak")
        ema = res.fetchall()
        return ema

    def getGakoGaldera(self):
        res = self.cur.execute("SELECT gakoGaldera FROM Erabiltzaileak")
        ema = res.fetchall()
        return ema

    def getGako(self):
        res = self.cur.execute("SELECT gakoa FROM Erabiltzaileak")
        ema = res.fetchall()
        return ema

    def ezabatuErabiltzailea(self,erabiltzailea):
        self.cur.execute("DELETE FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        self.con.commit()

    def puntuakEguneratu(self,erabiltzailea,tamaina,abiadura,puntuak):
        self.cur.execute("UPDATE ErabiltzailePuntuazioa SET puntuKop=(?) WHERE erabiltzailea=(?) AND tamaina=(?) AND abiadura=(?)", (puntuak, erabiltzailea,tamaina,abiadura))
        self.con.commit()

    def getPuntuak(self,erabiltzailea,tamaina,abiadura):

        res = self.cur.execute("SELECT puntuKop FROM ErabiltzailePuntuazioa WHERE erabiltzailea=(?) AND tamaina=(?) AND abiadura=(?)",
                               (erabiltzailea,tamaina,abiadura))
        puntuak = res.fetchone()
        return puntuak[0]

    def getErabiltzaileaRanking(self):
        res = self.cur.execute("SELECT erabiltzailea FROM ErabiltzailePuntuazioa")
        ema = res.fetchall()
        return ema

    def getTamainaRanking(self):
        res = self.cur.execute("SELECT tamaina FROM ErabiltzailePuntuazioa")
        ema = res.fetchall()
        return ema

    def getAbiaduraRanking(self):
        res = self.cur.execute("SELECT abiadura FROM ErabiltzailePuntuazioa")
        ema = res.fetchall()
        return ema

    def getpuntuakRanking(self):
        res = self.cur.execute("SELECT puntuKop FROM ErabiltzailePuntuazioa")
        ema = res.fetchall()
        return ema


    def getRankingAbsolutua(self):
        res = self.cur.execute("SELECT * FROM ErabiltzailePuntuazioa ORDER BY puntuKop DESC")
        ema = res.fetchall()
        return ema

    def getRankingX(self,tamaina, abiadura):
        res = self.cur.execute("SELECT erabiltzailea, puntuKop FROM ErabiltzailePuntuazioa WHERE tamaina=(?) AND abiadura=(?) ORDER BY puntuKop DESC ",
                               (tamaina,abiadura))
        ema = res.fetchall()
        return ema