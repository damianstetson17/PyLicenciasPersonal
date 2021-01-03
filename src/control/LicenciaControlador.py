from src.modelo import Licencia


class LicenciaControlador():
    __empleados = list()


    def getListaEmpleados(self):
        return self.__empleados
        
    #Persona
    def buscarPersona(self, nroLegajoBuscado):
        empleadoBuscado = None
        for e in self.__empleados:
            if(e.getNroLegajo() == nroLegajoBuscado):
                empleadoBuscado=e
                break
        return empleadoBuscado 

    def addPersona(self, newEmpleado):
        empleadoRepetido=None
        empleadoRepetido=self.buscarPersona(newEmpleado.getNroLegajo())
        # si no está repetido el nro de legajo
        if(empleadoRepetido==None):
            self.__empleados.append(newEmpleado)
            print(f"interté el empleado {newEmpleado.getNombreApe()} con nro de legajo {newEmpleado.getNroLegajo()}")
        else:
            print("Ocurrio un error al intentar crear el empleado (Ya existe un empleado con el mísmo nro de legajo)")    

    def delPersona(self, nroLegajoBuscado):
        personaBorrar=self.buscarPersona(self,nroLegajoBuscado)
        if(personaBorrar!=None):
            personaBorrar.setEstado(False)
        else:
            print("Ocurrio un error al intentar dar de baja el empleado (No se encontró el empleado con el nro de legajo)")  


    #dias correspondientes
    def generarDias_correspondiente(self, nroLegajoBuscado, diasCorrespNew):
        empleado=self.buscarPersona(nroLegajoBuscado)
        if(empleado!=None):
            diasDuplicado = empleado.buscarDias_correspondiente(diasCorrespNew.getFecha())
            if(diasDuplicado==None):#si no esta repetido
                empleado.addDias_correspondiente(diasCorrespNew)
                print(f"inserté el día correspondiente: {diasCorrespNew.getFecha()} con {diasCorrespNew.getDias()} "
                      f"días disponibles al legajo nro {nroLegajoBuscado}")
            else:
                print("Ocurrio un error al intentar dar días al empleado (Ya existen esos días asociados al nro de legajo)")
        else:
            print("Ocurrio un error al intentar dar días al empleado (No se encontró el empleado con el nro de legajo)")

    def bajaDias_correspondiente(self, nroLegajoBuscado, diasCorrespBaja):
        empleado=self.buscarPersona(self, nroLegajoBuscado)
        if(empleado!=None):
            if(empleado.buscarDias_correspondiente(diasCorrespBaja) != None):
                empleado.buscarDias_correspondiente(diasCorrespBaja).setEstado(False)
            else:
                print("Ocurrio un error al intentar dar de baja los días al empleado (No se encontraron los días")
        else:
            print("Ocurrio un error al intentar dar de baja los días al empleado (No se encontró el empleado con el nro de legajo)")

    #Licencias

        # función que verifica si es posible los días que se quiere tomar el empleado
    def verificarCantidadDiasLic(self, diasCorrespTotalesEmple, NewLicencia):
        verifica = False
        totalDiasDisponibles = 0
        diasPedidos = NewLicencia.getCantDias()
        for d in diasCorrespTotalesEmple:
            if (d.getEstado() == True):  # si son ocupables
                totalDiasDisponibles += d.getDias()
                if (totalDiasDisponibles >= diasPedidos):  # si dispongo de la cantidad usable de días
                    verifica = True
                    print(f"Existen suficientes días disponibles para generar la licencia solicitada ({totalDiasDisponibles} "
                          f"contados) hasta mayor o igual a {diasPedidos} días pedidos en la licencia")
                    break
        return verifica

    # función que controla y llama a insertar la licencia
    def generarLicencia(self, nroLegajoBuscado, newLicencia):
        empleado = self.buscarPersona(nroLegajoBuscado)
        if (empleado != None):
            licdupli = empleado.buscarLicencia(newLicencia.getFecha_ini(), newLicencia.getFecha_fin())
            if (licdupli is None):  # si la Lic no existe
                if (self.verificarCantidadDiasLic(empleado.getDias_correspondiente(), newLicencia) == True):#si hay suficientes dias para la lic
                    self.buscarPersona(nroLegajoBuscado).getLicencias().append(self.insertarLicencia(nroLegajoBuscado, newLicencia))
                else:
                    print("Ocurrio un error al intentar generar licencia al empleado (No se encontró el empleado con el nro de legajo)")
            else:
                print(
                    "Ocurrio un error al intentar generar licencia al empleado (Ya existe la licencia)")

    def insertarLicencia(self, nroLegajoBuscado, newLicencia):
        empleado = self.buscarPersona(nroLegajoBuscado)
        diasPedidos = newLicencia.getCantDias()
        diasPedidosCorresp = 0
        # recorremos los días correspondientes del empleado
        for dias in empleado.getDias_correspondiente():
            while ((diasPedidos > 0) and (dias.getEstado() == True)):  # si no se tomaron la cantidad de días para la lic, y ese dia corresp
                diasPedidos = diasPedidos - 1  # tiene aun dias tomables(se setea sola el estado en false si llega a cero)
                dias.setDias(dias.getDias() - 1)
                diasPedidosCorresp = diasPedidosCorresp + 1
            # cuando se terminan los de esos días se registra en la lista de lincencia de q años se tomaron los dias
            newLicencia.addFecha_de_anio(dias)
            print(f"se tomaron {diasPedidosCorresp} dias del año {dias.getFecha()}")
            diasPedidosCorresp = 0
            if (diasPedidos == 0):
                print(
                    f"La licencia del día {newLicencia.getFecha_ini()} ya tomo todos los días necesarios ({newLicencia.getCantDias()})")
                break  # si ya se llego a los dias pedidos, salimos del bucle (más óptimo)
        return newLicencia