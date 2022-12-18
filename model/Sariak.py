from controller.konexioa import Konexioa

class Sariak(object):

    __instance=None

    def __new__(cls):
        if Sariak.__instance is None:
            Sariak.__instance=object.__new__(cls)
        return Sariak.__instance

    def getMailakoSariPuntuak(self,tamaina,abiadura):
        return Konexioa().getMailakoSariPuntuak(tamaina, abiadura)


    def getSariId(self, tamaina, abiadura, partidaKop):
        return Konexioa().getSariId(tamaina, abiadura, partidaKop)