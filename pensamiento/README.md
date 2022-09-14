# Curso de introduccion al pensamiento probabilistico

![](https://static.platzi.com/cdn-cgi/image/width=768,quality=50,format=auto/media/achievements/badge-introduccion-pensamiento-probabilistico-e80a0071-01ca-4d27-b49d-67b9c94ae258.png "Logo del curso")

- [Curso de introduccion al pensamiento probabilistico](#curso-de-introduccion-al-pensamiento-probabilistico)
  - [Programacion probabilística](#programacion-probabilística)
    - [Introducción a la programacion probabilistica](#introducción-a-la-programacion-probabilistica)
    - [Probabilidad condicional](#probabilidad-condicional)
    - [Teorema de bayes](#teorema-de-bayes)
  - [Mentiras estadística](#mentiras-estadística)
    - [Garbage in, garbage out](#garbage-in-garbage-out)
    - [Imagenes engañosas](#imagenes-engañosas)
    - [Cum Hoc Ergo Propter Hoc](#cum-hoc-ergo-propter-hoc)
    - [Prejuicio en el muestreo](#prejuicio-en-el-muestreo)
    - [Falacia del francotirador de Texas](#falacia-del-francotirador-de-texas)
    - [Porcentajes confusos](#porcentajes-confusos)
    - [Falacia de regresión](#falacia-de-regresión)
  - [Introduccion al machine learning](#introduccion-al-machine-learning)
    - [Introduccion al machine learning](#introduccion-al-machine-learning-1)
    - [Feature vectors](#feature-vectors)
    - [Metricas de distancia](#metricas-de-distancia)
  - [Agrupamiento](#agrupamiento)
    - [Introduccion al agrupamiento](#introduccion-al-agrupamiento)
    - [Agrupamiento jerarquico](#agrupamiento-jerarquico)
    - [Agrupamiento K-means](#agrupamiento-k-means)
  - [Clasificación](#clasificación)
    - [Introduccion a la clasificacion](#introduccion-a-la-clasificacion)
    - [Clasificacion K-nearest neighbors](#clasificacion-k-nearest-neighbors)
___
## Programacion probabilística
### Introducción a la programacion probabilistica

> En la programacion probabilistica utilizamos modelos para poder obtener probabilidades. Tenemos librerias las cuales creamos ensima lenguajes de programacion como pyro de uber.

Un ejemplo es uber, crearon un programa que estima el tiempo de llegada del coche al usuario, esto lo hace mediante probabilidad, teniendo en cuenta diferentes variables como el trafico, la hora, etc. En coclusion la probabilidad nos ayuda a tener un magen de ayuda muy grande, como todo tenemos extremos y la verdad que la mayoria de nosotros estamos en la mitad asi que esto es importanticimo.

Mira mientras mas condiciones añadas a una probabilidad reducimos mas las opciones, piensalo. Un conjunto de estudiantes que es mas probable que haya estudiantes de ecuador en hardware o que haya estudiantes de ecuador y de quito en hardware, bueno lo que hicimos es reducir nuestras posibilidades. Les dejo un apoyo:

![](https://static.platzi.com/media/user_upload/intro_progra-7a4e645a-2434-4395-90a6-f27bf8485be9.jpg)

### Probabilidad condicional

> La probabilidad es la posibilidad que pase un suceso de entre un conjunto de posibilidades. Si tenemos eventos los cuales son independientes como lanzar una moneda o girar la ruleta cada tiro o giro no depende del anterior. Es decir, si cae cara no significa que haya mas probabilidad en la siguiente que caiga cruz, siempre tienen la misma probabilidad.

Como su nombre te lo dice es una probabilidad que te da unas condiciones o una serie de pasos que debe cumplir, para ese caso que quieres ejemplo. Encuentra los factores de 20 pero que siempre haya un 5 y un 2: Esto es una condicion solo hay un camino y es <5 * 2 * 2>.

**La formula de probabilidad es:**
P(A AND B) = P(A)P(A | B)

### Teorema de bayes

> Se base en como añadimos porcentaje a nuestra probabilidad de casos, sabiendo solo una cantidad limitada de datos, es decir con ejemplo. Si lanzamos una pelota a un balde o un hoyo y no sabes donde cayo, y luego lanzamos otra y tu medices que cayo delante o atras como puedo incorprar estos datos a mi set de probabilidad. Eso es lo que resolvio este teorema.

**El famoso teorema de bayes:**
P(A | B) = P(B|A)P(A)/P(B)

Utilizando probabilidad en un programa real de [python](./sintomas.py)
Datos que utilizamos ![datos de probabilidad](https://static.platzi.com/media/user_upload/yes-eb7a39ab-94b1-4d13-91a2-e99b495bda2a.jpg)

```python
# P(A | B) = P(B|A)P(A)/P(B)

def calc_bayes(prior_a, prob_b_dado_a, prob_b):
    return (prior_a * prob_b_dado_a) / prob_b


if __name__ == '__main__':
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer
    
    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)
    
    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    
    print(prob_cancer_dado_sintoma)
```

***Cuando los hechos cambian, yo cambio mi opinion, Que hace usted señor?***

---

## Mentiras estadística

### Garbage in, garbage out

>Tenemos varios bugs, si nos vamos por niveles los errores que tocaremos son los de tercer nivel son aquellos que estan en el diseño de la forma en que pensamos y llegamos a conclusiones.

GIGO **significa que si le metes basura, te devolvera basura**. La calidad de nuestros datos es igual de importante que nuestros computos, si metes datos erroneos tus resultados tambien seran errados.

### Imagenes engañosas

>Tener conclusiones precipidates despues de ver una imagen, estas te pueden engañar ya que es muy facil hacer imagenes que estan sesgadas de datos incorrectos, si una imagen no tiene etiquetas las tiras a la basura. Esta informacion no te sirve.

Los errores son muy comunes y presentan graficas que estan hechas para sacar conclusiones incorrectas, sesgando y omitiendo algunos de los datos importantes para su conveniencia.

### Cum Hoc Ergo Propter Hoc

>Una correlacion entre dos variables no significa causalidad, es decir, correlacion solo significa que dos cariables se mueven en un mismo sentido. El error es asignar causalidad en una correlacion.

Lo que significa es **despues de esto, eso; entonces a consecuencia de esto, eso.**

Piensa en un molino electrico o a motor hay varios factores correlacionales que hace que se mueva pero no significa que sean la causalidad, una persona adentro de este puede ayudar pero no es una causalidad directa. En este ejmplo solo tenemos una correlacion.

### Prejuicio en el muestreo

>Cuando no tenemos una muestra aleatoria y representativa, nuestro resultado esta sesgado y no aplica para el caso general de la poblacion, es decir, que se escoje los datos que quiere con un tema o un topico en especifico y eso significa que no hay aleatoriedad y peor rrepresentatividad.

Piensa quieres hacer un estudio de la poblacion, y lo unica poblacion que entrevistas son estudiantes universitarios, esto estaria bien si quieres el comportamiento o lo que sea que busques de solo estudiantes pero para toda la poblacion no aplica.

### Falacia del francotirador de Texas

>Lo que pasa aqui es que no tenemos en cuenta la aleatoriedad en nuestros datos, como lo indica el nombre es un francotirador el cual tiene un objetivo especifico para apuntarle.

Aqui algo que hacen es empesar a recojer datos antes de tener una hipotesis y esto es un error, ya que lo que te plnates va a estar sesgada en tus datos, ya que solo tienes datos que tu escojiste y sin aleatoriedad. Es como si disparas a una pare de madera y despues de disparas empiesas a pintar los circulos de objetivo en cada disparo. Este ejemplo es absurdo pero asi es como funciona esta falacia.

### Porcentajes confusos

>Si no te dicen de donde salen los porcentajes no puedes extraer conclusiones, no te dan algo tan importante como el contexto.

Hay ejemplos solo piensa en que si no te dan el contexto no puedes llegar a nada ya que puede ser un persentaje de lo que sea, y cuando digo lo que sea es lo que sea, incluso un estudio de personas que son mayores en tecnologia y le ponene porcentajes de personas que compran pan, esto es absurdo y es la forma mas simple de manipular los

### Falacia de regresión

>Lo que pasa es que pensamos que despues de un evento extremo, va a volver a pasar otro evento igual de extremo. Es decir, en montecarlo cayo nose tantas veces negros seguidos que la gente pierdo mucho dinero pensando que va a salir rojo la misma cantidad y esto es falso lo unico que pasa es que volvemos a la probabilidad normal o media de esos datos.

Normalmente cuando un evento fluctua existe una regresion a la media, lo cual es lo normal, como en todo hay sucesos o eventos los cuales pueden ser extremos pero despues siempre se regresa a la media.

---

## Introduccion al machine learning

### Introduccion al machine learning

>Es el campo de estudio que les da a las computadoras la habilidad de aprender sin ser explicitamente programadas.

Se basa en utilizar probabilidad para llegar a mejores conclusiones y resultados. Los cuales son sorprendentes cada vez me sorprende mas, y la verdad no se que nos depare en el futuro pero quiero ser uno de los desarrolladores.

### Feature vectors

>Es la forma de recojer algunas de las caracteristicas de los objetos de input para que los algoritmos puedan funcionar.

Debemos saber que es lo importante para modelar nuestra realidad, es decir, si quieres modelar un celula o proteina que es lo importante para eso puede ser el numero de atomos o de que compuesto esta hecho, su forma, etc. Sabes es endenter cuales son las caracteristicas de vectores mas importantes de ese objeto para ser moldeado.

### Metricas de distancia

>Nos dejan saber que tan lejanos o cercanos estan los vectores de nuestro algoritmo entre ellos.

Lo que buscan la mayoria de algoritmos es optimizar esta distancia entre vectores. Debes saber cual tipo de distancia que necesitas, porque si hay mas de un tipo de dsitancia como el de manhatan que se base en ir por las calles como si fuera una linea recta la cual no puede atravesar los edificios.

---
## Agrupamiento

### Introduccion al agrupamiento

>Los algoritmos de agrupamiento nos dejan entender la estructura interna de los datos cuando no es necesario añadir etiquetas, tambien agrupamos cada uno de nuestros datos para entender que tan similares son cada uno.

Para mas informacion de estos algoritmos les dejo un [articulo](https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68) que esta super bueno, si no dominas ingles puedes traducirlo de manera muy sencilla con google translator.

### Agrupamiento jerarquico

>Lo que hace es cojer un punto con otro y comparar la distancia y juntarlos en un conjunto si estan cercanos de manera iterativa.

Es interesante este algoritmo ya que conforme vamos agrupando, se construye un grafico de endograma que nos muestra una relacion interezante.

### Agrupamiento K-means

>Agrupa en grupos al hacer de manera que cada ves este va aprendiendo como los agrupa y llega a un punto donde ya no puede agrupar mas, es decir, es la solucion.

Lo importante es saber cuantos grupos son los que necesito, si no se cuantos grupos son puede que tengamos un resultado erroneo. Mira aqui debes saber que puedes utilizar un muestreo de los datos porque este algoritmo es muy pesado y te llevara demasiado tiempo ya que su forma de crecer puede que este entre exponencial y cuadrada asi que buena suerte. [Articulo](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://www.it.uc3m.es/~jvillena/irc/practicas/08-09/06.pdf) para entender mejor como funciona este algoritmo.

---

## Clasificación

### Introduccion a la clasificacion

Basicamente lo que hace es asignar a que grupo pertenece un dato que es desconocido. Este se utiliza mas en el aprendizaje supervizado. Para que se entienda mejor les dejo este [blog.](https://blog.bismart.com/la-clasificaci%C3%B3n-y-la-clusterizaci%C3%B3n-una-explicaci%C3%B3n-pr%C3%A1ctica)

### Clasificacion K-nearest neighbors

Este es uno de los metodos de clasificacion mas usados y antiguos, parte de que ya tenemos una base de clasificacion y queremos añadir nuevos datos y este los puede clasificar en que prupo pertenece nuestros datos. Por si les queda dudas aqui les dejo un [video](https://www.youtube.com/watch?v=eOhTuHAU5Uk).

>La base esta en comparar las distancias y la mas cercana es la que gana y le une a ese conjunto. Estos algoritmos son muy costosos asi que ya sabes debes usar una muestra representativa y aleatoria.