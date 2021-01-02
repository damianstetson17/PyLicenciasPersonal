from datetime import date
import datetime
from src.control import Licencia_controlador
from src.modelo import Persona, Dia_correspondiente, Licencia

controlador = Licencia_controlador.Licencia_controlador()
empleado1 = Persona.Persona(1, "Namis", datetime.datetime(2021, 1, 1))
empleado2 = Persona.Persona(2, "Angy", datetime.datetime(2021, 1, 1))
controlador.addPersona(empleado1)
controlador.addPersona(empleado2)
#generamos 10 días del año actual al empleado nro legajo 1
diasNew = Dia_correspondiente.Dia_correspondiente(datetime.datetime(2021, 3, 1), 10, True)
controlador.generarDias_correspondiente(1, diasNew)
diasDupli = Dia_correspondiente.Dia_correspondiente(datetime.datetime(2021, 3, 1), 10, True)
controlador.generarDias_correspondiente(1, diasDupli)

namis = controlador.buscarPersona(1)
for d in namis.getDias_correspondiente():
    print(d.getFecha())
    print(d.getDias())
diasList=list(namis.getDias_correspondiente())
print(len(diasList))

#licNew = Licencia.Licencia(date.today(), date.today()+datetime.timedelta(days=5), date.today())
#controlador.generarLicencia(1, licNew)
#namisLic = namis.getLicencias()
#print(namis.getLicencias())
