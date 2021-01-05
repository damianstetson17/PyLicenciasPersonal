"""""
TESTING THINGS, IGNORE ALL (OR WATCHES FOR CURIOSITY)

class ControladorLic:
        #función que verifica si es posible los días que se quiere tomar el empleado
        def verificarCantidadDiasLic(self, diasCorrespTotalesEmple, NewLicencia):
            verifica=False
            totalDiasDisponibles=0
            diasPedidos=NewLicencia.getCantDias()
            for d in diasCorrespTotalesEmple:
                if(d.getEstado() == True):#si son ocupables
                    totalDiasDisponibles+=d.getDias()
                    if(totalDiasDisponibles >= diasPedidos):#si dispongo de la cantidad usable de días
                        verifica=True
                        break
            return verifica

        #función que controla y llama a insertar la licencia
        def generarLicencia(self, nroLegajoBuscado, newLicencia):
            empleado=self.buscarPersona(nroLegajoBuscado)
            if(empleado!=None):
                if(self.verificarCantidadDiasLic(empleado.getDias_correspondiente(),newLicencia))==True):
                    self.insertarLicencia(nroLegajoBuscado, newLicencia)
            else:
                print("Ocurrio un error al intentar generar licencia al empleado (No se encontró el empleado con el nro de legajo)")

        def insertarLicencia(self, nroLegajoBuscado, newLicencia):
            empleado=self.buscarPersona(nroLegajoBuscado)
            diasPedidos=newLicencia.getCantDias()
            diasPedidosCorresp=0
            #recorremos los días correspondientes del empleado
            for dias in empleado.getDias_correspondiente():
                while ((diasPedidos>=0) and (dias.getEstado()==True)):#si no se tomaron la cantidad de días para la lic, y ese dia corresp
                    diasPedidos=diasPedidos-1                        #tiene aun dias tomables(se setea sola el estado en false si llega a cero)
                    dias.setDias(dias.getDias()-1)
                    diasPedidosCorresp=diasPedidosCorresp+1
                #cuando se terminan los de esos días se registra en la lista de lincencia de q años se tomaron los dias
                newLicencia.addFecha_de_anio(dias)
                print(f"se tomaron {diasPedidosCorresp} dias del año {dias.getFecha()}")
                diasPedidosCorresp=0
                if(diasPedidos==0):
                    print(f"La licencia del día {newLicencia.getFecha_ini()} ya tomo todos los días necesarios ({newLicencia.getCantDias()})")
                    break#si ya se llego a los dias pedidos, salimos del bucle (más óptimo)

        def calcularFechaFin(self, newLicencia):
            cantDiasPedidosAuxCont=newLicencia.getCantDiasPedidos()
            newFechaFin=newLicencia.getFechaFin()
            while(cantDiasPedidosAuxCont>0):
                #sumamos un día a la fecha inicial
                newFechaFin=newFechaFin + datetime.timedelta(days=1)
                cantDiasPedidosAuxCont=cantDiasPedidosAuxCont-1
                #si es sábado o domingo, hay que incrementar la fecha una vez más, el empleado no puede volver un fin de semana
                if(newFechaFin.weekday() > 5): #si es sábado o domingo, incrementamos otro día, pero no restamos al contador
                    newFechaFin = newFechaFin + datetime.timedelta(days=1)
                #recorremos la lista de feriados, el empleado no puede volver un feriado
                for feriado in self.__feriados:
                    if(feriado == newFechaFin):
                        #si es un día feriado, hay que incrementar el día, pero no el contador, un empleado no puede volver un feriado
                        newFechaFin = newFechaFin + datetime.timedelta(days=1)
            #guardamos la nueva fecha en la licencia
            newLicencia.setFechaFin(newFechaFin)
            return newLicencia"""""