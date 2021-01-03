from datetime import date
import datetime
from src.control import LicenciaControlador
from src.modelo import Persona, DiaCorrespondiente, Licencia

if (__name__ == "__main__"):

    controlador = LicenciaControlador.LicenciaControlador()

    print("##################################INICIO CREAR EMPLEADOS (Main)##################################\n")                                                     #año,mes,día
    empleado1 = Persona.Persona(1, "Namis", datetime.datetime(2021, 1, 1))
    empleado2 = Persona.Persona(2, "Angy", datetime.datetime(2021, 1, 1))
    controlador.addPersona(empleado1)
    controlador.addPersona(empleado2)

    print("##################################INICIO DIAS CORRESPONDIENTES (Main)##################################\n")
    #generamos 10 días del año 2021 actual al empleado nro legajo 1
    diasNew = DiaCorrespondiente.DiaCorrespondiente(datetime.datetime(2021, 3, 1), 10, True)
    controlador.generarDias_correspondiente(1, diasNew)
    #generamos 25 días del año 2009 actual al empleado nro legajo 1
    diasNew2 = DiaCorrespondiente.DiaCorrespondiente(datetime.datetime(2009, 2, 1), 25, True)
    controlador.generarDias_correspondiente(1, diasNew2)


    #pedimos una licencia de 15 días (debería ocupar las 10 del 2021 y 5 del 2009)
    print("##################################INICIO LICENCIA CORRECTA (Main)##################################\n")
    licNew = Licencia.Licencia(datetime.datetime(2021, 3, 1), datetime.datetime(2021, 3, 16))
    controlador.generarLicencia(1, licNew)

    # pedimos una licencia de 5 días (debería ocupar 5 del 2009)
    licMay = Licencia.Licencia(datetime.datetime(2021, 5, 1),datetime.datetime(2021, 5, 6))
    controlador.generarLicencia(1,licMay)

    # pedimos una licencia de 15 días (debería ocupar 5 del 2009)
    licJun = Licencia.Licencia(datetime.datetime(2021, 6, 1), datetime.datetime(2021, 5, 16))
    controlador.generarLicencia(1, licJun)

    print("##################################INICIO LICENCIA REPETIDA (Main)##################################\n")
    licdupli = Licencia.Licencia(datetime.datetime(2021, 3, 1), datetime.datetime(2021, 3, 6))
    controlador.generarLicencia(1, licdupli)


    #imprime los empleados y sus licencias asociadas
    for empleado in controlador.getListaEmpleados():
        print(
            f"\nCantidad de licencias generadas al empleado '{empleado.getNombreApe()}' nro legajo: "
            f"'{empleado.getNroLegajo()}'")
        print(f"Licencias de {empleado.getNombreApe()}:")
        lisLic = list(empleado.getLicencias())
        for lic in lisLic:
            print(f"\ttiene la Licencia del {lic.getFecha_ini().strftime('%d/%m/%Y')} con {lic.getCantDias()} días")
        print("\tTotal Licencias: ",len(lisLic))
