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

---

## Conceptos avanzados de funciones

### Clases

---

## Manejo de errores

### Clases

---

## Manejo de archivos

### Clases