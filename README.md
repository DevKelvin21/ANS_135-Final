# **ANALISIS NUMERICO CON PYTHON 3:**

- Creado por estudiantes de la Universidad de El Salvador.
- Resuelve problemas mediante metodos numericos para obtener las raices de funciones.
- Esta construido sobre python3.
- para la interfaz grafica nos auxiliamos de PyQt5, debido a que proporciona el editor 	Qt Desingner.
- Empaquetamos cada uno de los modulos que conforman los metodos numericos de nuestro programa para mejorar el flujo de trabajo y visual dentro de nuestro proyecto. 
- Se está trabajando con formularios y las opciones graficas basicas que ofrece Pyqt5
- Este programa puede mejorarse a una version web, utilizando los modulos existentes.
- Este programa utiliza en algunos objetcs (label,combobox,textfield) Y  una fuente de tetxo personalizada llamada "Space Mono Nerd Font" 
- Se anexo el archivo de instalacion de dicha fuente para windows 10 en el directorio docs/fonts

##  Tecnologias Utilizadas:

- [QtDesigner](https://www.qt.io/ "QtDesigner") 
- [Python3](https://www.python.org/ "Python3")  
- [PyQt5](https://pypi.org/project/PyQt5/ "PyQt5")

##  Recursos de la Web:

- [SpaceMonoNF](https://www.nerdfonts.com/ "SpaceMonoNF")
- [Flaticon](https://www.flaticon.es "Iconos")

## Librerias Necesarias

####    Ejecuta lo siguiente en el cmd de windows

`cmd /K C:\Users\"%USERNAME%"\AppData\Local\Programs\Python\Python39\python -m pip install numpy matplotlib sympy PyQt5`


####    En la consola de Linux o Mac

`$~ pip install PyQt5`

`$~ pip install sympy`

`$~ pip install numpy`

`$~ pip install matplotlib`

####    En caso de existir algun error colocar un numero 3 posterior a cada 'pip' comando, ejemplo:

`$~ pip3 install PyQt5`

##    Estructura del programa

- El directorio principal contiene dos subdirectorios mas los cuales son /docs y /src 
- En /src se encuentra todo el codigo de nuestro programa, a su vez /src esta subdividido en dos carpetas mas /Interfaz /modulos
- /modulos es un paquete el cual tiene todos los modulos necesarios para realizar todos los metodos numericos
- En /modulos se encuentran cada uno de los ficheros correspondientes a cada unidad en los cuales respectivamente estan los metodos de cada unidad. Existe un moculo llamado globalfunctions.py en el se encuentran aquellas funciones que validan los campos de texto del formulario, reciben como parametros el contenido de los lineEdit y devuelven la palabra "Error" si es que el campo esta vacio, sino devuelven el mismo valor pero convertido a flotante para que sea mas facil operarlo  
- En /Interfaz se encuentra el modulo perteneciente al formulario, en el se declaran todos los objetos se instancian y tambien las funciones o metodos que regulan el funcionamiento del mismo.

####    ¿Que ocurre al ejecutar el programa?

- se ejecuta una ventana con la mayoria de objetos ocultos y un menu de botones a la izquiera, debes seleccionar una unidad y una label te indicara en la parte superior en que unidad te encuentras, luego  deberas seleccionar un metodo de la unidad elegida, los metodos disponibles apareceran en un combobox  en la parte superior central de la ventana, al momento de seleccionar cualquiera se mostraran los elementos necesarios para la correcta realizacion del mismo.
- Se ingresan los datos en los campos disponibles y si es el caso se marcan las opciones como radiobuttons o combobox al finalizar se presiona el boton 'Resolverlo' al hacerlo este invoca a su vez al metodo correspondiente creado para cada unidad llamado 'Tabla_Unidad_(Numero de la unidad)' el cual se conecta con los modulos correspondientes y luego crea la tabla e inserta los datos obtenidos de las listas que envian los modulos. 

### Diagrama de Secuencias
                    
```seq
formMain->modulos: envia parametros
Note right of modulos: modulos recibe parametros\ny evalua la funcion
modulos-->formMain: devuelve el resultado
formMain->>modulos: gracias!
Note left of formMain: Muestra los datos\nen tabla
```


##    En Caso de querer modificar la interfaz

- Deberás abrir /docs/fromMain.ui con QtDesigner, realizas y guardas tus cambios.
- Tendras que convertir el archivo .ui a un .py para esto deberas usar algunos comandos.
- Tambien debes convertir el .qrc de las imagenes a .py para que el programa sepa leer las imagenes que usaste en tu formulario.

####    Ejecuta lo siguiente en tu terminal

`$~ pyrcc5 -o (NombreArchivo.py) (NombreArchivo.qrc)`
`$~ pyuic5 -x (NombreArchivo.ui)  -o (NombreArchivo.py)`

##    Cosas a tener en cuenta

- Luego de convertir nuestros archivos, deberas editar el nuevo (NombreArchivo.py) que corresponde al formulario deberas agregar todos los metodos que validan su funcionamiento y eliminar el main que viene por defecto al final del modulo, ya que tenemos un main mas limpio  construido.
- No debes cambiar el nombre de los objetcs, si lo haces es probable que algunas funciones no esten disponibles y el archivo no compile correctamente
- si agregas nuevos objects o nuevas funcionalidades debes implementarlas y crear los metodos correspondientes si lo ameritan.


### Fin