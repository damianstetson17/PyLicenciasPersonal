import datetime

from src.modelo import Licencia
from src.modelo.DiasTomados import DiasTomados
from src.modelo.Persona import Persona


class LicenciaControlador():
    __empleados = list()
    __feriados = list()

    def getListaFeriados(self):
        return self.__feriados

    def setListaFeriados(self, newListFeriados):
        self.__feriados=newListFeriados

    def getListaEmpleados(self):
        return self.__empleados

    #Feriados
    def buscarFeriado(self, feriadoBuscado):
        print("\t└->LLAMADO AL MÓDULO BUSCAR FERIADO")
        feriadoEncontrado = None
        for feriado in self.__feriados:
            if(feriado == feriadoBuscado):
                feriadoEncontrado=feriado
                break
        print(f"\t\t└>Retorno feriado buscado con el valor '{feriadoEncontrado}'")
        return feriadoEncontrado

    def addFeriado(self,NewFeriado):
        print("\t└->LLAMADO AL MÓDULO CREAR FERIADO")
        feriadoRepetido=self.buscarFeriado(NewFeriado)
        if(feriadoRepetido == None):
            self.__feriados.append(NewFeriado)
            print(f"\t\t└>Se insertó el feriado '{NewFeriado.strftime('%d/%m/%Y')}'")
        else:
            print(f"\t\t└>Ocurrió un error al intentar crear el feriado"
                  f" (Ya existe un feriado con la fecha'{NewFeriado.strftime('%d/%m/%Y')}')\n")

    #Persona
    def buscarPersona(self, nroLegajoBuscado):
        print("\t└->LLAMADO AL MÓDULO BUSCAR EMPLEADO")
        empleadoBuscado = None
        for e in self.__empleados:
            if(e.getNroLegajo() == nroLegajoBuscado):
                empleadoBuscado=e
                break
        print(f"\t\t└>Retorno el empleado buscado '{empleadoBuscado}'")
        return empleadoBuscado 

    def addPersona(self, newEmpleado):
        print("\t└->LLAMADO AL MÓDULO CREAR EMPLEADO")
        empleadoRepetido=None
        empleadoRepetido=self.buscarPersona(newEmpleado.getNroLegajo())
        # si no está repetido el nro de legajo
        if(empleadoRepetido==None):
            self.__empleados.append(newEmpleado)
            print(f"\t\t└>Se insertó el empleado '{newEmpleado.getNombreApe()}' con nro de legajo '{newEmpleado.getNroLegajo()}'\n")
        else:
            print(f"\t\t└>Ocurrio un error al intentar crear el empleado (Ya existe un empleado con el mísmo nro de legajo '{newEmpleado.getNroLegajo()}')\n")


    def delPersona(self, nroLegajoBuscado):
        print("\t└->LLAMADO AL MÓDULO BAJA EMPLEADO")
        personaBorrar=self.buscarPersona(self,nroLegajoBuscado)
        if(personaBorrar!=None):
            personaBorrar.setEstado(False)
            print(f"\t\t└>Se colocó el estado de '{personaBorrar.getEstado()}' al empleado '{personaBorrar.getNombreApe()}'"
                  f" con nro de legajo '{personaBorrar.getNroLegajo()}'")
        else:
            print(f"\t\t└>Ocurrio un error al intentar dar de baja el empleado (No se encontró el empleado con el nro de legajo '{nroLegajoBuscado}')")


    #dias correspondientes
    def generarDias_correspondiente(self, nroLegajoBuscado, diasCorrespNew):
        print("\t└->LLAMADO AL MÓDULO GENERAR DÍAS CORRESPONDIENTES")
        empleado=self.buscarPersona(nroLegajoBuscado)
        if(empleado!=None):
            diasDuplicado = empleado.buscarDias_correspondiente(diasCorrespNew.getFecha())
            if(diasDuplicado==None):#si no esta repetido
                empleado.addDiasCorrespondiente(diasCorrespNew)
                print(f"\t\t└>Se insertó el día correspondiente del año '{diasCorrespNew.getFecha().strftime('%Y')}' con '{diasCorrespNew.getDias()}'"
                      f" días disponibles al legajo nro '{nroLegajoBuscado}'\n")
            else:
                print(f"\t\t└>Ocurrio un error al intentar dar días al empleado (Ya existen días asociados al año '{diasCorrespNew.getFecha().strftime('%Y')}' al nro de legajo)")
        else:
            print(f"\t\t└>Ocurrio un error al intentar dar días al empleado (No se encontró el empleado con el nro de legajo '{nroLegajoBuscado}')")


    def bajaDias_correspondiente(self, nroLegajoBuscado, diasCorrespBaja):
        print("\t└->LLAMADO AL MÓDULO BAJA DÍAS CORRESPONDIENTES")
        empleado=self.buscarPersona(self, nroLegajoBuscado)
        if(empleado!=None):
            if(empleado.buscarDias_correspondiente(diasCorrespBaja) != None):
                empleado.buscarDias_correspondiente(diasCorrespBaja).setEstado(False)
                print(f"\t\t└>Se colocó el estado de '{empleado.buscarDias_correspondiente(diasCorrespBaja).getEstado()}'"
                      f"al día correspondiente del año "
                      f"'{empleado.buscarDias_correspondiente(diasCorrespBaja).getFecha().strftime('%Y')}'")
            else:
                print(f"\t\t└>Ocurrio un error al intentar dar de baja los días al empleado (No se encontraron los días del año '{diasCorrespBaja.getFecha().strftime('%Y')}'")
        else:
            print(f"\t\t└>Ocurrio un error al intentar dar de baja los días al empleado (No se encontró el empleado con el nro de legajo '{nroLegajoBuscado}')")

    #Licencias

        # función que verifica si es posible los días que se quiere tomar el empleado
    def verificarCantidadDiasLic(self, diasCorrespTotalesEmple, NewLicencia):
        print("\t\t└->LLAMADO AL MÓDULO VERIFICAR CANT DIAS LIC ")
        verifica = False
        totalDiasDisponibles = 0
        diasPedidos = NewLicencia.getDifDias()
        for d in diasCorrespTotalesEmple:
            if (d.getEstado() == True):  # si son ocupables
                totalDiasDisponibles += d.getDias()
                if (totalDiasDisponibles >= diasPedidos):  # si dispongo de la cantidad usable de días
                    verifica = True
                    print(f"\t\t\t└>Existen suficientes días disponibles para generar la licencia solicitada "
                          f"existen mayor o igual a '{diasPedidos}' días pedidos en la licencia ('{totalDiasDisponibles}' existentes)\n")
                    break
        if(verifica==False):
            print(f"\t\t\t└>No existen suficientes días disponibles para generar la licencia solicitada"
                  f" (La licencia '{NewLicencia.getFechaIni().strftime('%d/%m/%Y')}' requiere '{NewLicencia.getDifDias()}' días)\n")
        return verifica

    # función que controla y llama a insertar la licencia
    def generarLicencia(self, nroLegajoBuscado, newLicencia):
        print("\t└->LLAMADO AL MÓDULO GENERAR LICENCIA")
        empleado = self.buscarPersona(nroLegajoBuscado)
        if (empleado != None):
            licdupli = empleado.buscarLicencia(newLicencia.getFechaIni(), newLicencia.getFechaFin())
            if (licdupli is None):  # si la Lic no existe
                if (self.verificarCantidadDiasLic(empleado.getDiasCorrespondienteList(), newLicencia) == True):#si hay suficientes dias para la lic
                    #le damos su fecha fin
                    newLicencia=self.calcularFechaFin(newLicencia)
                    empleado.getLicencias().append(self.insertarDiasALicencia(nroLegajoBuscado, newLicencia))
                    print(f"\t\t└>Se insertó la licencia del '{newLicencia.getFechaIni().strftime('%d/%m/%Y')}' al empleado '{empleado.getNombreApe()}'\n")
            else:
                print(f"\t\t└>Ocurrio un error al intentar generar licencia al empleado"
                      f" (Ya existe una licencia con la fecha '{newLicencia.getFechaIni().strftime('%d/%m/%Y')}')\n")


    def insertarDiasALicencia(self, nroLegajoBuscado, newLicencia):
        print("\t└->LLAMADO AL MÓDULO INSERTAR LICENCIA")
        empleado = self.buscarPersona(nroLegajoBuscado)
        cantDiasPedidos = newLicencia.getCantDiasPedidos()
        diasPedidosCorresp = 0
        # recorremos los días correspondientes del empleado
        for dias in empleado.getDiasCorrespondienteList():
            while ((cantDiasPedidos > 0) and (dias.getEstado() == True)):  # si no se tomaron la cantidad de días para la lic, y ese dia corresp
                cantDiasPedidos = cantDiasPedidos - 1  # tiene aun dias tomables(se setea sola el estado en false si llega a cero)
                dias.setDias(dias.getDias() - 1)
                diasPedidosCorresp = diasPedidosCorresp + 1
            # cuando se terminan los de esos días se registra en la lista de lincencia de q años se tomaron los dias
            if(diasPedidosCorresp>0):
                diasTomados = DiasTomados(diasPedidosCorresp,dias.getFecha())#generamos los dias tomados
                newLicencia.addDiasTomados(diasTomados)
                print(f"\t\t└>Se tomaron '{diasTomados.getCantidadDiasTomados()}' dias del año '{diasTomados.getAnioDiasCorresp().strftime('%Y')}'")
            for dTomadosEnLic in newLicencia.getDiasTomados():
                anio = dTomadosEnLic.getAnioDiasCorresp()
                print(f"\t\t\t└>La licencia '{newLicencia.getFechaIni().strftime('%d/%m/%Y')}' tiene '{dTomadosEnLic.getCantidadDiasTomados()}' días "
                      f"del año '{anio.strftime('%Y')}'")
            diasPedidosCorresp = 0
            if (cantDiasPedidos == 0):
                print(
                    f"\t\t└>La licencia del día '{newLicencia.getFechaIni().strftime('%d/%m/%Y')}' ya tomo todos los días necesarios ('{newLicencia.getDifDias()}' días)")
                break  # si ya se llego a los dias pedidos, salimos del bucle (más óptimo)
        return newLicencia

    def calcularFechaFin(self, newLicencia):
        print("\t└->LLAMADO AL MÓDULO CALCULAR FECHA FIN LICENCIA")
        cantDiasPedidosAuxCont = newLicencia.getCantDiasPedidos()-1 #-1 porque comienza desde ese día
        newFechaFin = newLicencia.getFechaFin()
        while (cantDiasPedidosAuxCont > 0):
            # si es sábado o domingo, hay que incrementar la fecha una vez más, el empleado no puede volver un fin de semana
            if (newFechaFin.weekday() >= 5):
                # si es sábado o domingo, incrementamos otro día, pero no restamos al contador
                newFechaFin = newFechaFin + datetime.timedelta(days=1)

            #el empleado tampoco puede volver un feriado
            else:
                if(newFechaFin in self.__feriados):
                    # si es un día feriado, hay que incrementar el día, pero no el contador, un empleado no puede volver un feriado
                    newFechaFin = newFechaFin + datetime.timedelta(days=1)

                else:
                    # si es un dia útil sumamos un día a la fecha inicial, y restamos uno a los que se piden de licencia
                    newFechaFin = newFechaFin + datetime.timedelta(days=1)
                    cantDiasPedidosAuxCont = cantDiasPedidosAuxCont - 1

        # guardamos la nueva fecha en la licencia
        newLicencia.setFechaFin(newFechaFin)
        print(f"\t\t└>Retorno la licencia (Del '{newLicencia.getFechaIni().strftime('%d/%m/%Y')}') "
              f"con su nueva fecha final calculada: '{newLicencia.getFechaFin().strftime('%d/%m/%Y')}'")
        return newLicencia