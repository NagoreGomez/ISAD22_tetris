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
            "CREATE TABLE IF NOT EXISTS ErabiltzailePuntuazioa(erabiltzailea,abiadura,tamaina,puntuMax,unekoPuntuak,partidaKop)")

        res = self.cur.execute("SELECT * FROM ErabiltzailePuntuazioa  WHERE erabiltzailea='admin'")

        if res.fetchone() is None:
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','1','1',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','1','2',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','1','3',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','2','1',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','2','2',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','2','3',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','3','1',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','3','2',0,0,0)")
            self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES ('admin','3','3',0,0,0)")



        #sariakkk
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Sariak(id,abiadura,tamaina,puntuKop,partidaKop)")

        res = self.cur.execute("SELECT * FROM Sariak")
        self.cur.execute("DELETE FROM Sariak")
        if res.fetchone() is None:
            self.cur.execute("INSERT INTO Sariak VALUES ('1','1','1','300','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('2','1','1','300','4')")
            self.cur.execute("INSERT INTO Sariak VALUES ('3','1','2','300','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('4','1','2','300','4')")
            self.cur.execute("INSERT INTO Sariak VALUES ('5','1','3','300','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('6','1','3','300','4')")

            self.cur.execute("INSERT INTO Sariak VALUES ('7','2','1','200','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('8','2','1','200','4')")
            self.cur.execute("INSERT INTO Sariak VALUES ('9','2','2','200','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('10','2','2','200','4')")
            self.cur.execute("INSERT INTO Sariak VALUES ('11','2','3','200','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('12','2','3','200','4')")

            self.cur.execute("INSERT INTO Sariak VALUES ('13','3','1','100','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('14','3','1','100','4')")
            self.cur.execute("INSERT INTO Sariak VALUES ('15','3','2','100','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('16','3','2','100','4')")
            self.cur.execute("INSERT INTO Sariak VALUES ('17','3','3','100','2')")
            self.cur.execute("INSERT INTO Sariak VALUES ('18','3','3','100','4')")

            # erabiltzaileSariak
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS ErabiltzaileSariak(erabiltzailea,saria)")
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


    def erabiltzaileaGehitu(self,izena,erabiltzailea,email,pasahitza,gakoGaldera,gakoa,fondoa,adreiluak,soinua,puntuak, partida):
        self.cur.execute("INSERT INTO Erabiltzaileak VALUES(?, ?, ?,?,?,?,?,?,?,?,?)",
                    (erabiltzailea, izena, email, pasahitza, gakoGaldera, gakoa,fondoa,adreiluak,soinua,puntuak, partida))

        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)",(erabiltzailea, '1','1',0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '1', '2',0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '1', '3', 0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '2', '1', 0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '2', '2', 0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '2', '3', 0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '3', '1', 0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '3', '2', 0,0,0))
        self.cur.execute("INSERT INTO ErabiltzailePuntuazioa VALUES(?, ?, ?,?,?,?)", (erabiltzailea, '3', '3', 0,0,0))

        self.con.commit()


    def konexioa_itxi(self):
        self.con.close()

    def getErabiltzaileaInfo(self,erabiltzailea):
        res = self.cur.execute("SELECT * FROM Erabiltzaileak WHERE erabiltzailea=(?)", (erabiltzailea,))
        return res.fetchone()



    def pertsonalizazioaGorde(self,erabiltzailea):
        self.cur.execute("UPDATE Erabiltzaileak SET fondoa=(?), adreiluak=(?), soinua=(?) WHERE erabiltzailea=(?)",  (erabiltzailea.fondoa,erabiltzailea.adreiluak,erabiltzailea.soinua,erabiltzailea.erabiltzailea))
        self.con.commit()



    def partidaGorde(self,erabiltzailea):
        self.cur.execute("UPDATE Erabiltzaileak SET partida=(?), puntuak=(?) WHERE erabiltzailea=(?)",
                         (erabiltzailea.partida, erabiltzailea.puntuak, erabiltzailea.erabiltzailea))
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

    def pasahitzaAldatu(self,erabiltzailea):
        self.cur.execute("UPDATE Erabiltzaileak SET pasahitza=(?) WHERE erabiltzailea=(?)",(erabiltzailea.pasahitza, erabiltzailea.erabiltzailea))
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
        self.cur.execute("DELETE FROM ErabiltzailePuntuazioa WHERE erabiltzailea=(?)", (erabiltzailea,))
        self.cur.execute("DELETE FROM ErabiltzaileSariak WHERE erabiltzailea=(?)", (erabiltzailea,))

        self.con.commit()

    def puntuakEguneratu(self,erabiltzailea,tamaina,abiadura,puntuak):
       self.cur.execute("UPDATE ErabiltzailePuntuazioa SET puntuMax=(?) WHERE erabiltzailea=(?) AND tamaina=(?) AND abiadura=(?)", (puntuak, erabiltzailea,tamaina,abiadura))
       self.con.commit()

    def getPuntuak(self,erabiltzailea,tamaina,abiadura):

        res = self.cur.execute("SELECT puntuMax FROM ErabiltzailePuntuazioa WHERE erabiltzailea=(?) AND tamaina=(?) AND abiadura=(?)",
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
        res = self.cur.execute("SELECT puntuMax FROM ErabiltzailePuntuazioa")
        ema = res.fetchall()
        return ema


    def getMailakoSariPuntuak(self,tamaina,abiadura):
        res = self.cur.execute(
            "SELECT puntuKop FROM Sariak WHERE tamaina=(?) AND abiadura=(?)",
            (tamaina, abiadura))
        puntuak = res.fetchone()
        return puntuak[0]

    def getErabiltzailearenMailakoPartidaKop(self,tamaina,abiadura,erabiltzailea):
        res = self.cur.execute(
            "SELECT partidaKop FROM ErabiltzailePuntuazioa WHERE tamaina=(?) AND abiadura=(?) AND erabiltzailea=(?)",
            (tamaina, abiadura,erabiltzailea))
        partidaKop = res.fetchone()
        return partidaKop[0]



    def unekoPuntuakEguneratu(self,tamaina,abiadura,puntuak,partidaKop,erabiltzailea):
        self.cur.execute(
            "UPDATE ErabiltzailePuntuazioa SET unekoPuntuak=(?), partidaKop=(?) WHERE tamaina=(?) AND abiadura=(?) AND erabiltzailea=(?)",
            (puntuak,partidaKop,tamaina, abiadura,erabiltzailea))
        self.con.commit()



    def getSariId(self, tamaina, abiadura, partidaKop):
        res =self.cur.execute("SELECT id FROM Sariak WHERE tamaina=(?) AND abiadura=(?) AND partidaKop=(?) ",(tamaina,abiadura,partidaKop))
        id = res.fetchone()
        return id[0]





    def erabiltzaleariSariaEman(self, id, erabiltzailea):
        self.cur.execute("INSERT INTO ErabiltzaileSariak VALUES(?, ?)",(erabiltzailea, id));
        self.con.commit()


    def getErabiltzaileak(self):
        res = self.cur.execute("SELECT distinct (erabiltzailea,puntuMax) FROM ErabiltzailePuntuazioa ORDER BY puntuMax DESC")
        erab = res.fetchall()
        print(erab)
        return erab

    def getErabiltzaileInfo(self, erabiltzailea):
        print(erabiltzailea)
        res = self.cur.execute("SELECT MAX(puntuMax),tamaina,abiadura FROM ErabiltzailePuntuazioa WHERE erabiltzailea=(?)",(erabiltzailea,))
        info = res.fetchall()
        return info

    def getRankingAbsolutua(self):
        res = self.cur.execute(
            "SELECT  erabiltzailea,tamaina,abiadura,max(puntuMax) FROM ErabiltzailePuntuazioa GROUP BY erabiltzailea ORDER BY puntuMax DESC;")
        info = res.fetchall()
        return info


    def getRankingX(self,tamaina, abiadura):
        res = self.cur.execute("SELECT erabiltzailea,puntuMax FROM ErabiltzailePuntuazioa WHERE tamaina=(?) AND abiadura=(?) ORDER BY puntuMax DESC ",
                               (tamaina,abiadura))
        ema = res.fetchall()
        return ema
