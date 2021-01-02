from datetime import datetime


class Licencia():
    # construct
    def __init__(self, fecha_ini, fecha_finNew):
        self.__fecha_inicio = fecha_ini
        self.__fecha_fin = fecha_finNew

        self.__fecha_de_anios = list()

    # setters
    def setFecha_ini(self, fecha_ini):
        self.__fecha_inicio = fecha_ini

    def setFecha_fin(self, fecha_finNew):
        self.__fecha_fin = fecha_finNew

    def setFecha_de_anio(self, fecha_anio):
        self.__fecha_de_anio = fecha_anio

    def addFecha_de_anio(self, fecha_anioNew):
        self.__fecha_de_anios.append(fecha_anioNew)

    # getters
    def getFecha_ini(self):
        return self.__fecha_inicio

    def getFecha_fin(self):
        return self.__fecha_fin

    def getFecha_de_anio(self):
        return self.__fecha_de_anio

    def getCantDias(self):
        return abs((self.__fecha_inicio - self.__fecha_fin).days)
