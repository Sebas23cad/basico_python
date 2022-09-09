# Curso de introduccion al pensamiento probabilistico

![](https://static.platzi.com/cdn-cgi/image/width=768,quality=50,format=auto/media/achievements/badge-introduccion-pensamiento-probabilistico-e80a0071-01ca-4d27-b49d-67b9c94ae258.png "Logo del curso")

___
## Programacion probabilística
#### Introducción a la programacion probabilistica

> En la programacion probabilistica utilizamos modelos para poder obtener probabilidades. Tenemos librerias las cuales creamos ensima lenguajes de programacion como pyro de uber.

Un ejemplo es uber, crearon un programa que estima el tiempo de llegada del coche al usuario, esto lo hace mediante probabilidad, teniendo en cuenta diferentes variables como el trafico, la hora, etc. En coclusion la probabilidad nos ayuda a tener un magen de ayuda muy grande, como todo tenemos extremos y la verdad que la mayoria de nosotros estamos en la mitad asi que esto es importanticimo.

Mira mientras mas condiciones añadas a una probabilidad reducimos mas las opciones, piensalo. Un conjunto de estudiantes que es mas probable que haya estudiantes de ecuador en hardware o que haya estudiantes de ecuador y de quito en hardware, bueno lo que hicimos es reducir nuestras posibilidades. Les dejo un apoyo:

![](https://static.platzi.com/media/user_upload/intro_progra-7a4e645a-2434-4395-90a6-f27bf8485be9.jpg)

#### Probabilidad condicional

> La probabilidad es la posibilidad que pase un suceso de entre un conjunto de posibilidades. Si tenemos eventos los cuales son independientes como lanzar una moneda o girar la ruleta cada tiro o giro no depende del anterior. Es decir, si cae cara no significa que haya mas probabilidad en la siguiente que caiga cruz, siempre tienen la misma probabilidad.

Como su nombre te lo dice es una probabilidad que te da unas condiciones o una serie de pasos que debe cumplir, para ese caso que quieres ejemplo. Encuentra los factores de 20 pero que siempre haya un 5 y un 2: Esto es una condicion solo hay un camino y es <5 * 2 * 2>.

**La formula de probabilidad es:**
P(A AND B) = P(A)P(A | B)

#### Teorema de bayes

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

#### garbage
---

## Introduccion al machine learning

---
## Agrupamiento

---
## Clasificación