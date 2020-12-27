from datetime import datetime, date

class Persona():
    #construct
    def __init__(self,nroAgregar,nombreApe,antiNew):
        
        self.__nro_legajo=nroAgregar
        self.__nombre_apellido=nombreApe
        self.__antiguedad=antiNew

    #attributes
    __nro_legajo = 0
    __nombre_apellido = ""
    __antiguedad = datetime.now()
    __licencias = list()
    __dias_correspondientes = list()
    __activo = True

#setters
def setNro_legajo(self, nroAgregar):
   self.__nro_legajo=nroAgregar

def setNombre_apellido(self, nombreApe):
   self.__nombre_apellido=nombreApe

def setAntiguedad(self, antiNew):
   self.__antiguedad=antiNew

def setEstado(self, estado):
   self.__activo=estado

def addDias_correspondiente(self, diasNew):
   self.__dias_correspondientes.append(diasNew)

#getters
def getNroLegajo(self):
   return self.__fech__nro_legajoa_inicio

def getNombreApe(self):
   return self.__nombre_apellido

def getAntiguedad(self):
   return self.__antiguedad

def getEstado(self):
   return self.__activo

def getDias_correspondiente(self):
   return self.__dias_correspondientes