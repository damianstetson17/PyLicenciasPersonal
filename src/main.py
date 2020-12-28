from datetime import date
from Licencias.src import Licencia_controlador, Persona

controlador = Licencia_controlador.Licencia_controlador()
empleado1 = Persona.Persona(1,"Namis",date.today())
empleado2 = Persona.Persona(2,"Angy",date.today())
controlador.addPersona(empleado1)
controlador.addPersona(empleado2)
for e in controlador.getListaEmpleados():
    print(e.getNombreApe())