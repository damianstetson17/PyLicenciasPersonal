# 👥 PyLicenciasPersonal 👥
Sistema de gestión de licencias para un departamento de personal, en donde se lleva registro y control de licencias de empleados, en el podrás:

* Crear y borrar empleados basados en un identificador denominado "número de legajo".
* Crear y borrar dias correspondientes por año.
* Crear Licencias.
* Llevar registro de licencias y días correspondientes de empleados.
* Generar Excel con informe

## Diagrama de Clases
Se decidió realizar el proyecto en base al paradigmas orientado a objetos, por lo tanto, se adjunta el diagrama de clases asociado a la resolución del escenario, esto también afectó la manera de organización de los módulos y clases del proyecto [(Véase la carpeta raíz del código)](https://github.com/damianstetson17/PyLicenciasPersonal/tree/main/src).

![diagrama_de_clases](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/classes.jpeg)

## ⚠️ Estado del proyecto ⚠️

El proyecto aún se encuentra **en desarrollo**.

### Hecho ✅:
* Modelo completo.
* Logger en consola de los llamados a los módulos y mensajes de errores.
![errors and msj](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/msj_errors.png)

### En desarrollo 🛠️:
* No contabilizar *días feriados* ni *fines de semana* a la hora de contabilizar los días de licencia
* Caducidad de días correspondientes no utilizados en *X* cantidad de tiempo en desarrollo.
* Graphic user interface.
* Generación de Excels.


## 🚀 ¿Cómo ejecutar? 🚀

Para ejecutar correctamente simplemente compilar el archivo [main.py](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/src/main.py) este contiene la instanciación de dos empleados _("Namis" y "Angy")_ quienes poseen sus números de legajo _("Namis" posee el número de legajo "1", "Angy" el número de legajo "2")_ seguido a estos se instanciarán dos días correspondientes al empleado "Namis", le corresponderán 10 días del año 2021 y 25 días del año 2009. Se solicitará generar dos Licencia, una de 15 días _(desde 1/03/21 al 16/03/21)_ y otra de 5 días _(desde 1/05/21 al 6/05/21)_.
Además se solicita una licencia extra, luego de haberse generado las dos anteriores que solicita 16 días al empleado "Namis", el cual no posee _(Ya que utilizó todos sus días disponibles en las dos licencias anteriores)_ a fin de generar una situación de error y poner el sistema a pruebas, el cual no generará dicha licencia. Ídem de esto es la generación de una licencia _"duplicada"_ ya que cuenta con en el mísmo día de inicio que una de las ya generadas _(esto generar una situación de error, un mismo empleado no debería poder solicitar dos licencias el mísmo día, por lo que el sistema tampoco la generará)_.

El mensaje mostrado por consola, de esta fracción del código al compilarse será:

![msj_lic](https://github.com/damianstetson17/PyLicenciasPersonal/blob/main/img/msj_gen_lic.png)

## 🐢 Aclaraciones 🐢

Si bien se han desarrollado métodos _"getters & setters"_ basados en la filosofía de un fuerte encapsulamiento  esto no tendrá nunca mísma filosofía de **Java**. Hay un concepto que describe bien la diferencias en este: La idea del _"Programador Malvado"_ _(Por favor no malinterpretar esto, es simplemente una metáfora)_, en Java hay un encapsulamiento muy fuerte en los objetos, ciertas propiedades las podemos acceder solo mediante los métodos apropiados, la idea es que en **Java** se cuida a los objetos de este hipotético _"Programador Malvado"_, en **Python** esa idea se la reemplaza por un: _"somos todos adultos"_, es decir cada uno sabe lo que está haciendo, si quieres modificar un atributo interno de un objeto, perfecto, se supone que sabes lo que estás haciendo. Por lo que se han generado métodos hipotéticos que incluso algunos no se utilizan dentro del projecto. 

_Todas estas imágenes y documentación se encuentran sujetas a cambios, que serán publicados en tiempo y forma._
