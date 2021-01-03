class DiasTomados:
    def __init__(self, cantidadTomados, anioDiasCorresp):
        self.cantidadDias=cantidadTomados
        self.anioDiasCorrespondiente=anioDiasCorresp

    #getters
    def getCantidadDiasTomados(self):
        return self.cantidadDias

    def getAnioDiasCorresp(self):
        return self.anioDiasCorrespondiente

    #setters
    def setCantidadDiasTomados(self, newCantDias):
        self.cantidadDias=newCantDias

    def setAnioDiasCorresp(self, newCanioDiasCorres):
        self.anioDiasCorrespondiente=newCanioDiasCorres