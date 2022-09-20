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

Ahora

---

## Conceptos avanzados de funciones

### Clases

---

## Manejo de errores

### Clases

---

## Manejo de archivos

### Clases