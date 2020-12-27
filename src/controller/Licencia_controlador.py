class Licencia_controlador():
    #construct
    def __init__(self, ListEmpleados):  
        self.__empleados=ListEmpleados

    __empleados = list()

#Persona
def buscarPersona(self, nroLegajoBuscado):
    empleadoBuscado = None
    for e in self.__empleados:
        if(e.getNroLegajo() == nroLegajoBuscado):
            empleadoBuscado=e
            break
    return empleadoBuscado 

def addPersona(self, newEmpleado):
    #si no está repetido el nro de legajo
    if(buscarPersona(self,newEmpleado.getNroLegajo())==None):
        self.__empleados.append(newEmpleado)   
    else:
        print("Ocurrio un error al intentar crear el empleado (Ya existe un empleado con el mísmo nro de legajo)")    

def delPersona(self, nroLegajoBuscado):
    personaBorrar=buscarPersona(self,nroLegajoBuscado)
    if(personaBorrar!=None):
        personaBorrar.setEstado(False)
    else:
        print("Ocurrio un error al intentar dar de baja el empleado (No se encontró el empleado con el nro de legajo)")  


#dias correspondientes
def generarDias_correspondiente(self, nroLegajoBuscado, diasCorrespNew):
    empleado=buscarPersona(self, nroLegajoBuscado)
    if(empleado!=None):
        diasDuplicado = empleado.buscarDias_correspondiente(diasCorrespNew)
        if(diasDuplicado==None):#si no esta repetido
            empleado.addDias_correspondiente(diasCorrespNew)
        else:
            print("Ocurrio un error al intentar dar días al empleado (Ya existen esos días asociados al nro de legajo)")
    else:
        print("Ocurrio un error al intentar dar días al empleado (No se encontró el empleado con el nro de legajo)")

def bajaDias_correspondiente(self, nroLegajoBuscado, diasCorrespBaja):
    empleado=buscarPersona(self, nroLegajoBuscado)
    if(empleado!=None):
        if(empleado.buscarDias_correspondiente(diasCorrespBaja) != None):
            empleado.buscarDias_correspondiente(diasCorrespBaja).setEstado(False)
        else:
            print("Ocurrio un error al intentar dar de baja los días al empleado (No se encontraron los días")
    else:
        print("Ocurrio un error al intentar dar de baja los días al empleado (No se encontró el empleado con el nro de legajo)")

#Licencias
def varificarDias(self, diasCorrespoBuscar,fecha_verificar):
    existe=False
    for d in diasCorrespoBuscar:
        if((d.getFecha() == fecha_verificar) and (d.getEstado()==True)):#si coincide las fechas de la lic con un dias corresp y está activo
            existe=True
            break
    return existe

def generarLicencia(self, nroLegajoBuscado, newLicencia):
    empleado=buscarPersona(self, nroLegajoBuscado)
    if(empleado!=None):
        if(empleado.buscarLicencia(newLicencia.getFecha_ini(),newLicencia.getFecha_fin()) == None):#si la Lic no existe
           #verificar que existe los dias correspondientes
            varificarDias(self,empleado.getDias_correspondiente(), newLicencia.getFecha_de_anio())
        else:
            print("Ocurrio un error al intentar generar licencia al empleado (Ya existe la licencia con esas fechas para el empleado con el nro de legajo)")
    else:
        print("Ocurrio un error al intentar generar licencia al empleado (No se encontró el empleado con el nro de legajo)")