from datetime import datetime


class Licencia():
    # construct
    def __init__(self, fecha_ini, fecha_fin):
        self.__fecha_inicio = fecha_ini
        self.__fecha_fin = fecha_fin
        self.__diasTomados = list()

    # setters
    def setFecha_ini(self, fecha_ini):
        self.__fecha_inicio = fecha_ini

    def setFecha_fin(self, fecha_finNew):
        self.__fecha_fin = fecha_finNew

    def setDiasTomados(self, diasTomadosNewList):
        self.__diasTomados = diasTomadosNewList

    def addDiasTomados(self, diasTomadosNew):
        self.__diasTomados.append(diasTomadosNew)

    # getters
    def getFecha_ini(self):
        return self.__fecha_inicio

    def getFecha_fin(self):
        return self.__fecha_fin

    def getDiasTomados(self):
        return self.__diasTomados

    def getCantDias(self):
        return abs((self.__fecha_inicio - self.__fecha_fin).days)
