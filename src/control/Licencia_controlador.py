from src.modelo import Licencia


class Licencia_controlador():
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
            print("interté el empleado ", newEmpleado.getNombreApe())
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
                print(f"inserté el día {diasCorrespNew.getFecha()} con {diasCorrespNew.getDias()} días disponibles al legajo nro {nroLegajoBuscado}")
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
    def varificarDias(self, diasCorrespoBuscar,fecha_verificar,cantDiasSolicitados):
        existe = False
        for d in diasCorrespoBuscar:
            if((d.getFecha() == fecha_verificar) and (d.getEstado()==True)):#si coincide las fechas de la lic con un dias corresp y está activo
                if(d.getDias()>=cantDiasSolicitados):#si los dias pedidos no superan a los posibles
                    existe = True
                    print("La licencia Verifica")
                    break
                else:
                    print("se agotaron los dias")
        return existe

    def generarLicencia(self, nroLegajoBuscado, newLicencia):
        empleado=self.buscarPersona(nroLegajoBuscado)
        if(empleado!=None):
            licdupli=empleado.buscarLicencia(newLicencia.getFecha_ini(),newLicencia.getFecha_fin())
            if(licdupli is None):#si la Lic no existe
            #verificar que existe los dias correspondientes, y puede pedir la cantidad de dias
                print("dif dias lic (osea cantidad de dias pedidos): ", newLicencia.getCantDias())
                if(self.varificarDias(empleado.getDias_correspondiente(), newLicencia.getFecha_de_anio(),newLicencia.getCantDias())==True):
                    #restamos los dias a los dias correspondientes del año pedidos en la licencia
                    dias_mod=empleado.buscarDias_correspondiente(newLicencia.getFecha_de_anio())
                    dias_mod.setDias(dias_mod.getDias()-newLicencia.getCantDias())
                    print(f"agregué la licencia {newLicencia.getFecha_ini()} al empleado {nroLegajoBuscado}")
                    print(f"Los dias corresp ({dias_mod.getFecha()} quedaron con {dias_mod.getDias()} dias)")
                    #agregamos la Licencia nueva a la persona
                    empleado.getLicencias().append(newLicencia)
                    if (dias_mod.getDias() == 0):
                        dias_mod.setEstado(False)  # si se quedo en cero, apagamos esos días corresp
                else:
                    print("Ocurrio un error al intentar generar licencia al empleado (No verifica)")
            else:
                print(
                    "Ocurrio un error al intentar generar licencia al empleado (Ya existe la licencia)")
        else:
            print("Ocurrio un error al intentar generar licencia al empleado (No se encontró el empleado con el nro de legajo)")