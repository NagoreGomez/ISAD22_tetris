from controller.konexioa import Konexioa
from model.Jokalaria import Jokalaria

class Jokalariak(object):

    __instance=None

    def __new__(cls):
        if Jokalariak.__instance is None:
            Jokalariak.__instance=object.__new__(cls)
        return Jokalariak.__instance

    def erabiltzailearenpasahitza(self,erabiltzailea):
        return Konexioa().erabiltzailearenPasahitza(erabiltzailea)

    def erabiltzaileaKonprobatu(self,erabiltzailea):
        return Konexioa().erabiltzaileaKonprobatu(erabiltzailea)

    def erabiltzaileaEtaPasahitzaKonprobatu(self,erabiltzailea,pasahitza):
        return Konexioa().erabiltzaileaEtaPasahitzaKonprobatu(erabiltzailea,pasahitza)

    def getErabiltzaileaInfo(self,erabiltzailea):
        info= Konexioa().getErabiltzaileaInfo(erabiltzailea)
        if info is not None:
            Jok=Jokalaria(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10])
            return Jok
        return None


    def erabiltzaileaGehitu(self,jokalaria):
        Konexioa().erabiltzaileaGehitu(jokalaria.erabiltzailea,jokalaria.izena,jokalaria.email,jokalaria.pasahitza,jokalaria.gakoGaldera,jokalaria.gakoa,jokalaria.fondoa,jokalaria.adreiluak,jokalaria.soinua,jokalaria.puntuak,jokalaria.partida)


    def ezabatuErabiltzailea(self,erabiltzailea):
        Konexioa().ezabatuErabiltzailea(erabiltzailea)

    def partidaKargatu(self,erabiltzailea):
        return Konexioa().partidaKargatu(erabiltzailea)

    def puntuakLortu(self, erabiltzailea):
        return Konexioa().puntuakLortu(self, erabiltzailea)


    def getErabiltzailea(self):
        return Konexioa().getErabiltzailea()

    def getIzena(self):
        return Konexioa().getErabiltzailea()

    def getEmail(self):
        return Konexioa().getEmail()

    def getPasahitza(self):
        return Konexioa().getPasahitza()

    def getGakoGaldera(self):
        return Konexioa().getGakoGaldera()

    def getGako(self):
        return Konexioa().getGako()



    def getPuntuak(self,erabiltzailea,tamaina,abiadura):
        return Konexioa().getPuntuak(erabiltzailea,tamaina,abiadura)


    def puntuakEguneratu(self,erabiltzailea,tamaina,abiadura,puntuak):
        Konexioa().puntuakEguneratu(erabiltzailea,tamaina,abiadura,puntuak)


    def getErabiltzailearenMailakoPartidaKop(self,tamaina,abiadura,erabiltzailea):
        return Konexioa().getErabiltzailearenMailakoPartidaKop(tamaina,abiadura,erabiltzailea)


    def unekoPuntuakEguneratu(self,tamaina,abiadura,puntuak,partidaKop,erabiltzailea):
        return Konexioa().unekoPuntuakEguneratu(tamaina,abiadura,puntuak,partidaKop,erabiltzailea)


    def erabiltzaleariSariaEman(self, id, erabiltzailea):
        Konexioa().erabiltzaleariSariaEman(id, erabiltzailea)


