from datetime import date
import datetime
from src.control import LicenciaControlador
from src.modelo import Persona, DiaCorrespondiente, Licencia

if (__name__ == "__main__"):

    controlador = LicenciaControlador.LicenciaControlador()
                                                            #año,mes,día
    empleado1 = Persona.Persona(1, "Namis", datetime.datetime(2021, 1, 1))
    empleado2 = Persona.Persona(2, "Angy", datetime.datetime(2021, 1, 1))
    controlador.addPersona(empleado1)
    controlador.addPersona(empleado2)
    #generamos 10 días del año actual al empleado nro legajo 1
    diasNew = DiaCorrespondiente.DiaCorrespondiente(datetime.datetime(2021, 3, 1), 10, True)
    controlador.generarDias_correspondiente(1, diasNew)
    print("#################FIN DIAS CORRESPONDIENTES#################")

    licNew = Licencia.Licencia(datetime.datetime(2021, 3, 1), datetime.datetime(2021, 3, 6))
    controlador.generarLicencia(1, licNew)
    namisLic = list(controlador.buscarPersona(1).getLicencias())
    print("Licencias:")
    print(len(namisLic))

    licdupli = Licencia.Licencia(datetime.datetime(2021, 3, 1), datetime.datetime(2021, 3, 6))
    controlador.generarLicencia(1, licdupli)
