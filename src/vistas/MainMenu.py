from tkinter import *

class VentanaPrincipal:

    def __init__(self, ancho,largo):
        self.__ventanaMenu = Tk()
        self.__ventanaMenu.geometry(f"{ancho}x{largo}+100+100")
        self.__ventanaMenu.title("Menú Principal")
        self.generarBarraMenu(self.__ventanaMenu)
        self.__ventanaMenu.mainloop()

    def generarBarraMenu(self,ventanaMenu):
        #barra de menús
        barraMenus = Menu(ventanaMenu)
        #menú cargar
        subMenuCargar = Menu(barraMenus)
        "sub menu empleado de 'subMenuCargar' "
        subMenuCargarEmpleado = Menu(subMenuCargar)
        subMenuCargarEmpleado.add_command(label="Cargar Manualmente")
        subMenuCargarEmpleado.add_command(label="Cargar por Tabla Excel")
        subMenuCargar.add_cascade(label="Nuevo Empleado", menu=subMenuCargarEmpleado)

        subMenuCargar.add_command(label="Nuevo Días Correspondientes a Empleado")

        "sub menu licencia de 'subMenuCargar' "
        subMenuCargarLicencia = Menu(subMenuCargar)
        subMenuCargarLicencia.add_command(label="Desde fecha inicio con cantidad días")
        subMenuCargarLicencia.add_command(label="Por días correspondientes específicos")
        subMenuCargar.add_cascade(label="Nueva Licencia", menu=subMenuCargarLicencia)

        subMenuCargar.add_separator()
        subMenuCargar.add_command(label="Nuevo Feriado")
        barraMenus.add_cascade(label="Cargar", menu=subMenuCargar)

        #menú modificar
        SubMenuModificiar = Menu(barraMenus)
        SubMenuModificiar.add_command(label="Empleado")
        SubMenuModificiar.add_command(label="Días correspondientes")
        SubMenuModificiar.add_command(label="Licencia")
        SubMenuModificiar.add_separator()
        SubMenuModificiar.add_command(label="Feriado")
        barraMenus.add_cascade(label="Modificar", menu=SubMenuModificiar)

        #menú baja
        SubMenuBaja = Menu(barraMenus)
        SubMenuBaja.add_command(label="Baja Empleado")
        SubMenuBaja.add_command(label="Baja Días Correspondientes de Empleado")
        SubMenuBaja.add_separator()
        SubMenuBaja.add_command(label="Baja de un Feriado")
        barraMenus.add_cascade(label="Baja", menu=SubMenuBaja)

        #menú exportar
        SubMenuExportar = Menu(barraMenus)
        SubMenuExportar.add_command(label="Generar Excel Empleados")
        SubMenuExportar.add_command(label="Generar Excel Licencias de un año")
        barraMenus.add_cascade(label="Exportar", menu=SubMenuExportar)

        # agregamos los menus a la barra de menu principal
        ventanaMenu.config(menu=barraMenus)
