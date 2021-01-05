from datetime import datetime


class Licencia():
    # construct
    def __init__(self, fecha_ini, cantDiasPedidosNew):
        self.__fecha_inicio = fecha_ini
        self.__cantDiasPedidos=cantDiasPedidosNew
        self.__fecha_fin =fecha_ini
        self.__diasTomados = list()

    # setters
    def setFechaIni(self, fecha_ini):
        self.__fecha_inicio = fecha_ini

    def setDiasPedidos(self, diasPedidosNew):
        self.__cantDiasPedidos=diasPedidosNew

    def setFechaFin(self, fecha_finNew):
        self.__fecha_fin = fecha_finNew

    def setDiasTomados(self, diasTomadosNewList):
        self.__diasTomados = diasTomadosNewList

    def addDiasTomados(self, diasTomadosNew):
        self.__diasTomados.append(diasTomadosNew)

    # getters
    def getFechaIni(self):
        return self.__fecha_inicio

    def getFechaFin(self):
        return self.__fecha_fin

    def getCantDiasPedidos(self):
        return self.__cantDiasPedidos

    def getDiasTomados(self):
        return self.__diasTomados

    def getDifDias(self):
        return abs((self.__fecha_inicio - self.__fecha_fin).days)
