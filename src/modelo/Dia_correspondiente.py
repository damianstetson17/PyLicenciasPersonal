from datetime import datetime, date


class Dia_correspondiente():
    # construct
    def __init__(self, fecha_anioNew, cantDias, estado):

        self.__fecha_anio = fecha_anioNew
        self.__dias = cantDias
        self.__activo = estado

    # attributes
    __fecha_anio = datetime.now()
    __dias = 0
    __activo = True

    # setters
    def setFecha(self, fecha_ini):
        self.__fecha_anio = fecha_ini

    def setDias(self, diasNew):
        self.__dias = diasNew
        if (self.__dias == 0):  # si se puso en cero, se da de baja
            self.__activo = False
        else:
            self.setEstado(True)

    def setEstado(self, estado):
        self.__activo = estado

    # getters
    def getFecha(self):
        return self.__fecha_anio

    def getDias(self):
        return self.__dias

    def getEstado(self):
        return self.__activo
