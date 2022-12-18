from controller.konexioa import Konexioa


class Jokalaria(object):

    def __init__(self,erabiltzailea, izena,email,pasahitza,gakoGaldera,gakoa,fondoa='#98F5FF',adreiluak='1',soinua='soinua1',puntuak=0,partida='/'):
        self.erabiltzailea=erabiltzailea
        self.izena=izena
        self.email=email
        self.pasahitza=pasahitza
        self.gakoGaldera=gakoGaldera
        self.gakoa=gakoa
        self.fondoa=fondoa
        self.adreiluak=adreiluak
        self.soinua=soinua
        self.puntuak=puntuak
        self.partida=partida



    def partidaGorde(self, partida, puntuak):
        self.puntuak=puntuak
        self.partida=partida
        Konexioa().partidaGorde(self)

    def pasahitzaAldatu(self, pasahitza):
        self.pasahitza=pasahitza
        Konexioa().pasahitzaAldatu(self)


    def pertsonalizazioaGorde(self, kolorea, adreiluak, soinua):
        self.fondoa=kolorea
        self.adreiluak=adreiluak
        self.soinua=soinua
        Konexioa().pertsonalizazioaGorde(self)

