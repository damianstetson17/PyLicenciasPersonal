from datetime import date
import datetime
from src.control.LicenciaControlador import LicenciaControlador
from src.modelo.Persona import Persona
from src.modelo.DiaCorrespondiente import DiaCorrespondiente
from src.modelo.Licencia import Licencia
from src.modelo.DiasTomados import DiasTomados

if (__name__ == "__main__"):

    controlador = LicenciaControlador()

    print("##################################INICIO CREAR EMPLEADOS (Main)##################################\n")                                                     #año,mes,día
    empleado1 = Persona(1, "Namis", datetime.datetime(2021, 1, 1))
    empleado2 = Persona(2, "Angy", datetime.datetime(2021, 1, 1))
    empleRepetido = Persona(1, "Namis", datetime.datetime(2021, 1, 1))
    controlador.addPersona(empleado1)
    controlador.addPersona(empleado2)
    controlador.addPersona(empleRepetido)

    print("##################################INICIO DIAS CORRESPONDIENTES (Main)##################################\n")
    # generamos 20 días del año 2021 actual al empleado nro legajo 1
    diasNew = DiaCorrespondiente(datetime.datetime(2021, 3, 1), 20, True)
    controlador.generarDias_correspondiente(1, diasNew)
    # generamos 15 días del año 2009 actual al empleado nro legajo 1
    diasNew2 = DiaCorrespondiente(datetime.datetime(2009, 2, 1), 15, True)
    controlador.generarDias_correspondiente(1, diasNew2)

    print("##################################INICIO CREAR FERIADOS (Main)##################################\n")
    feriado1=datetime.datetime(2021, 3, 3)
    controlador.addFeriado(feriado1)
    feriado2 = datetime.datetime(2021, 3, 4)
    controlador.addFeriado(feriado2)
    feriado3 = datetime.datetime(2021, 3, 5)
    controlador.addFeriado(feriado3)
    #feriado repetido
    feriadoRepetido = datetime.datetime(2021, 3, 3)
    controlador.addFeriado(feriadoRepetido)

    print(
        "##################################INICIO VENCIMIENTO DÍAS CORRESP (Main)##################################\n")
    # el orden de llamada al módulo cambiará que días se vencerán dependiendo si se han creado licencias antes
    # los días correspondientes del empleado que no hayan sido ocupados al menos en una licencia,
    # y sean viejos (menores al año especificado -normalmente, el año actual-) serán dados de baja
    controlador.actualizarVencimientosDiasCorresp(empleado1, 52)

    #pedimos una licencia de 15 días (debería ocupar las 10 del 2021 y 5 del 2009)
    print("##################################INICIO LICENCIA CORRECTA (Main)##################################\n")
    licNew = Licencia(datetime.datetime(2021, 3, 1), 15)
    controlador.generarLicencia(1, licNew)

    # pedimos una licencia de 5 días (debería ocupar 5 del 2009)
    licMay = Licencia(datetime.datetime(2021, 5, 1),5)
    controlador.generarLicencia(1,licMay)

    # pedimos una licencia de 15 días (debería ocupar 15 del 2009)
    licJun = Licencia(datetime.datetime(2021, 6, 1), 15)
    controlador.generarLicencia(1, licJun)

    print("##################################INICIO LICENCIA REPETIDA (Main)##################################\n")
    licdupli = Licencia(datetime.datetime(2021, 3, 1), 5)
    controlador.generarLicencia(1, licdupli)


    print("##################################INSERCIÓN DE LIC VIEJA (Main)##################################\n")
    licVieja = Licencia(datetime.datetime(2009, 1, 1),5)
    diasViejosOcupados = DiasTomados(5,diasNew2)
    controlador.agregarDiasCorrespALicencia(licVieja,diasViejosOcupados)
    empleado1.getLicencias().append(licVieja)

    print("##################################RESULTADOS FINALES (Main)##################################\n")
    #imprime los días feriados existente
    print("Feriados existentes:")
    for feriado in controlador.getListaFeriados():
        print(f"Existe el feriado '{feriado.strftime('%d/%m/%Y')}'")
    print(f"\tTotal Feriados: {len(controlador.getListaFeriados())} \n")

    #imprime los empleados y sus licencias asociadas
    for empleado in controlador.getListaEmpleados():
        print(
            f"Cantidad de licencias generadas al empleado '{empleado.getNombreApe()}' nro legajo: "
            f"'{empleado.getNroLegajo()}'")
        print(f"Licencias de {empleado.getNombreApe()}:")
        lisLic = list(empleado.getLicencias())
        for lic in lisLic:
            print(f"\t╚»tiene la Licencia del {lic.getFechaIni().strftime('%d/%m/%Y')} al '{lic.getFechaFin().strftime('%d/%m/%Y')}' con {lic.getCantDiasPedidos()} días")
        print(f"\tTotal Licencias: {len(lisLic)} \n")

    #imprimir días corresp por empleado
    for empleado in controlador.getListaEmpleados():
        print(f"Cantidad de días correspondientes del empleado '{empleado.getNombreApe()}'"
              f" nro de legajo '{empleado.getNroLegajo()}'")
        for dias in empleado.getDiasCorrespondienteList():
            print(f"\t╚»Año '{dias.getFecha().strftime('%Y')}' tiene '{dias.getDias()}' con el estado de '{dias.getEstado()}'")
        print("\n")