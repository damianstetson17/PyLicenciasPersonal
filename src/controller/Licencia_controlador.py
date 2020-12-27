class Licencia_controlador():
    #construct
    def __init__(self,ListEmpleados):  
        self.__empleados=ListEmpleados

    __empleados = list()

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

def addDias_correspondiente(self,nroLegajoBuscado, diasCorrespNew):
    empleado=buscarPersona(nroLegajoBuscado)
    if(empleado!=None):
        empleado