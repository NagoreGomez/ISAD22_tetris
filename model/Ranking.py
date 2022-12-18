from controller.konexioa import Konexioa


class Ranking(object):


    def getRankingAbsolutua(self):
        return Konexioa().getRankingAbsolutua()

    def getRankingX(self,tamaina, abiadura):
        return Konexioa().getRankingX(tamaina, abiadura)
