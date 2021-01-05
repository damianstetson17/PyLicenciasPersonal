from datetime import datetime, date

class Persona():
    #construct
    def __init__(self,nroAgregar,nombreApe,antiNew):
        
        self.__nro_legajo=nroAgregar
        self.__nombre_apellido=nombreApe
        self.__antiguedad=antiNew
        self.__licencias = []
        self.__dias_correspondientes = list()
        self.__activo = True

   #setters
    def setNroLegajo(self, nroAgregar):
      self.__nro_legajo=nroAgregar

    def setNombreApe(self, nombreApe):
      self.__nombre_apellido=nombreApe

    def setAntiguedad(self, antiNew):
      self.__antiguedad=antiNew

    def setEstado(self, estado):
      self.__activo=estado

    def addDiasCorrespondiente(self, diasNew):
      self.__dias_correspondientes.append(diasNew)
      #ordenamos la lista desde el año más viejo
      self.__dias_correspondientes=sorted(self.__dias_correspondientes, key=lambda x: x.getFecha())

   #getters
    def getNroLegajo(self):
      return self.__nro_legajo

    def getNombreApe(self):
      return self.__nombre_apellido

    def getAntiguedad(self):
      return self.__antiguedad

    def getEstado(self):
      return self.__activo

    def getDiasCorrespondienteList(self):
      return self.__dias_correspondientes

    def getLicencias(self):
      return self.__licencias

   #buscar
    def buscarDias_correspondiente(self, fecha_ini_busc):
      dias_buscados=None
      for d in self.__dias_correspondientes:
         if(d.getFecha()==fecha_ini_busc):
            dias_buscados=d
            break
      return dias_buscados

    def buscarLicencia(self, fecha_ini_busc, fecha_fin_busc):
      lic_buscados=None
      for l in self.__licencias:
         if((l.getFechaIni() == fecha_ini_busc)):
            lic_buscados=l
            break
      return lic_buscados

