# Curso de Python Intermedio: Comprehensions, Lambdas y Manejo de Errores

![Logo del curso](https://static.platzi.com/cdn-cgi/image/width=768,quality=50,format=auto/media/achievements/badge-intermedio-de-python-d0d16518-5edd-450a-b2a9-0710bded1494.png)

## Preparación antes de empezas

### El Zen de python

Son los 20 principios que tiene el lenguaje para escribir un codigo preciso y limpio. Aqui les dejo el [zen](https://peps.python.org/pep-0020/), Otra forma de verlo es con el comando import this, en la consola interactiva.

### Que es la documentación?

Es tu manual de usuario para saber como usar dicha tecnologia, aqui te da todas las especificaciones del como usarla con ejemplos. Aqui esta la [documentacion de python](https://docs.python.org/3/). Importante aqui tienes todas las herramientas para entender a profundida el lenguaje de manera mas tecnica mi recomendacion, has los cursos de platzi primero o cualquiera introductorios y despues ve a la documentacion.

---

## Entorno virtual

### Que es un entorno virtual?

Es un ambiente o una section la cual tiene instalado diferentes paquetes y modulos que se utilizan en ese proyecto, es decir, para cada proyecto tu creas tu ambiente miralo como un estadio o algo similar que sea gigante y que en el almacenas todo lo que necesitas para que funcione y haci sucesivamente en cada proyecto.

> Una analogia piensa que un ambiente es una ciudad de un pais y que diferente tiene cada pais, bueno cada uno tiene sus ciudades y su cultura pero todos estan hechos en espacios fisicos. Osea un ambiente ceria una ciudad y cada uno de esto tiene sus modulos y librerias en diferentes versiones que serian la cultura y las obras de arte.

Para crear un ambiente virtual con python lo que hacemos es lo siguiente:

`py -m venv venv or env`

Ahora tambien debemos prender el entorno:

`.\venv\scripts\activate`

El alias que creamos es el siguiente para activar nuestros ambientes:

`avenv`

Para desactivarlo:

`deactivate`

### Instalacion de dependencias con pip

Es un modulo que esta creado para instalar otros modulos que no vienen dentro de python. Package Installer for Python.
Para instalar cualquier modulo lo usamos asi,siempre utiliza pip activando el entorno virtual:

``` console
<!-- lista de paquetes instalados -->
pip freeze
<!-- instalar modulos -->
pip install libreria o modulo como pandas
<!-- Compartir archivos de dependencia con mas personas con un archivo-->
pip freeze > requeriments.txt
<!-- para instalar las dependencias del archivo -->
pip install -r requeriments.txt
```

---

## Alternativa a los ciclos: comprehensions

### Listas y diccionarios anidados

Lo que vamos a ver es como crear listas que lleven diccionarios y diccionarios que lleven listas el [codigo](list_and_dicts.py).

### list comprehensions

Tenemos un reto y el cual es crear una lista de los 100 primeros numeros naturales al cuadrado, es decir, hacer una especie de tabla de potenciacion de los numeros al cuadrado. Aqui esta mi solucion en [codigo](./numeros_cuadrado.py).
List comprehension es una estructura de python que se utiliza para crear nuevas listas, se puede o no poner la condicional, la estructura:

`[element for element in iterable if condition]`

El primer elemento representa cada uno de los elementos que se pondra en la lista, el ciclo a partir del cual se extraeran elementos de otra lista o un iterable, y al final la condicion para filtrar elementos del ciclo.
Aqui les dejo una imagen para que se entienda mejor:
![](https://miro.medium.com/max/2980/1*zJ0XfN1fkWSvll2Bg8o46g.png)
![](https://static.platzi.com/media/user_upload/List_comprehensions1-bacd6262-4bc3-40c8-8c71-3da952e30b41.jpg)
![](https://static.platzi.com/media/user_upload/List_comprehensions2-665fd48c-97a6-4ddb-939f-a0afcf5b8eda.jpg)

[Solucion](reto1.py) del reto que nos dejo al final del video.

### Dictionary comprehensions

Aqui les dejo el primer archivo que vamos a usar que es el [ejemplo](dicts_compre.py). Ahora es lo mismo que el anterior pero lo unico es que añadimos dos valores adelante y lo usamos para crear diccionarios mucho mas rapido y eficas.

![](https://static.platzi.com/media/user_upload/List_Dict_Comprehensions-478137d2-d3b8-4509-be4d-29eb0e455e8a.jpg). Aqui les dejo una imagen para que entiendan mejor, pero es muy sencillo.

Aqui les dejo mi [solucion](reto2.py) del reto.

---

## Conceptos avanzados de funciones

### Funciones anónimas: lambda

Son funciones las cuales no tienen un nombre o identificador, lo que le hace especial es la estructura
`lambda argumentos: expresión`
Los argumentos pueden ser todos los que necesesitemos pero solo puede tener una expresion o linea de codigo. Osea que puede tener todos los argumentos que quieras pero solo puede haber una linea de codigo. Aqui les dejo los ejemplos en [codigo](anonima_func.py) python.

![](https://runestone.academy/runestone/books/published/fopp/_images/lambda.gif)
![](https://i1.faceprep.in/Companies-1/python-lambda-functions-new.png)
Cosas importantes es que con el nombre que llamamos a la funcion es con el nombre de la variable en la cual lo almacenamos, ahora este no es el nombre podria ser como su clave de un diccionario. Osea que solo es para saber a que nos referimos, lo que hace es guardar la funcion anonima en el y cuando lo usamos simplemente hace la funcion. en lambda no es necesario colocar la palabra return para que nos devuelva algo, este por si solo nos devuelve un valor.

### High order functions: filter, map y reduce

Una funcion de orden superior es la que recibe como parametro otra funcion y hace algo con ella. Aqui tenemos que saber que hay tres de estas que estan en casi todos los lenguajes y entenderemos las diferencias: [aplicado en codigo](high_func.py)

- Filter:
  Usando la funcion filter podemos filtrar los datos de lo que queramos y esta recive dos parametro, el primero es otra funcion o la operacion que quieres que se realice y el segundo es a donde se va a realizar.
- Map:
  Basicamente usamos la misma logica de codigo que la de arriva, y lo que hacemos es recorrer la lista o el iterable y hacemos la operacion que nos indica en la funcion.
- Reduce:
  Lo que hacemos basicamente es reducir nuestros valores o lo que tengamos con una funcion que creamos, la sintaxis es un poquito diferente ya que tenemos dos parametros y lo unico es que cada ves que hacemos esa operacion y se guarda en el primer parametro y en el segundo se almacena el siguiente elemento de la lista y haci hasta acabar. Lo unico que debemos hacer es importar esto de los modulos de pythin al principio del codigo.

Notas y programa de la clase filtrar datos en [codigo](filtrar_datos.py).
Solucion del proyecto [filtrar datos.](filtrar_challenge.py)

---

## Manejo de errores

### Los errores en el codigo

Basicamente tenemos dos tipos de errores los que python nos avisa y los que no.
Los que nos avisa son dos tipos las exception y los syntaxError, que basicamente que basicamente hay un ponton de estos asi que mejor lean y con todo les dejo unas imagenes que lo entiendan mejor.
Ahora los que no nos avisa son aquellos los cuales son problemas de logica, ya que aqui necesitas repasarlo de pies a cabeza una ves para ver el error, a mi me pasa que me equivoco y pongo estos simbolos <>, cambiados, esto es error de logica nada mas.
Un consejo los errores siempre leelos del final hacia el principio, desde la ultima linea hasta el principio.
![Imagen de los slide de la clase](https://static.platzi.com/media/user_upload/error-62a56437-8b39-4cd9-85da-0dac5854ee3d.jpg)
![Apuntes para entenderlo mejor](https://static.platzi.com/media/user_upload/image_362-3ab90bf4-92f4-46b4-8b81-43e4e36b6f8f.jpg)

### Debugging

As

---

## Manejo de archivos

### Clases