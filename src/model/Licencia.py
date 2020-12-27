from datetime import datetime, date

class Licencia():
    #construct
    def __init__(self,fecha_ini,fecha_finNew):
        
        self.__fecha_inicio=fecha_ini
        self.__fecha_fin=fecha_finNew

    #attributes
    __fecha_inicio = datetime.now()
    __fecha_fin = datetime.now()

#setters
def setFecha_ini(self, fecha_ini):
   self.__fecha_inicio=fecha_ini

def setFecha_fin(self, fecha_finNew):
   self.__fecha_fin=fecha_finNew

#getters
def getFecha_ini(self):
   return self.__fecha_inicio

def getFecha_fin(self):
   return self.__fecha_fin