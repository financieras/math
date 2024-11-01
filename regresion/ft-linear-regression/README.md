# ft-linear-regression

Your first implementation of a machine learning algorithm.


# Regresión Lineal y Métodos de Optimización

## Introducción a la Regresión Lineal

- La **regresión lineal** es una de las técnicas fundamentales en estadística y aprendizaje automático. Su objetivo es modelar la relación entre una variable dependiente ($y$) y una o más variables independientes ($x$) mediante una función lineal.
- En nuestro caso estimaremos el precio de los coches de segunda mano en función del kilometraje que tengan. En nuestro caso existe una variable dependiente $y$ que es el precio y una única variable independiente $x$ que es el kilometraje.
- Cuando hay una única variable independiente hablamos de modelo de regresión lineal simple.

## Métodos de Resolución

### Mínimos Cuadrados Ordinarios (OLS)

El problema de la **regresión lineal** tradicionalmente se resuelve utilizando el método de los mínimos cuadrados ordinarios (OLS, por sus siglas en inglés). Este método es óptimo cuando la función de error a minimizar es convexa, lo cual ocurre en la regresión lineal simple. En estos casos, encontrar el mínimo es matemáticamente sencillo: se deriva la función de error y se iguala a cero, ya que en el punto mínimo la pendiente es horizontal.

### Descenso del Gradiente

En muchos otros problemas de optimización, la función de costes no es convexa, lo que hace necesario utilizar métodos alternativos para encontrar mínimos locales. El **algoritmo del descenso del gradiente** es el método iterativo más utilizado en aprendizaje automático para este propósito.

#### Conceptos Fundamentales del Descenso del Gradiente

1. **El Gradiente**:
   - Es un vector formado por las derivadas parciales de la función objetivo
   - Indica la dirección de máximo crecimiento de la función
   - Al multiplicarlo por -1, obtenemos la dirección de máximo decrecimiento
   
2. **Tasa de Aprendizaje ($\alpha$)**:
   - Es un hiperparámetro crucial que determina el tamaño de los pasos en cada iteración
   - Típicamente toma valores pequeños (ej: $\alpha = 0.01$)
   - Si es demasiado grande, el algoritmo puede diverger
   - Si es demasiado pequeña, la convergencia será muy lenta

## Ecuación de la Recta de Regresión

La recta de regresión se expresa matemáticamente como:

$$y = \theta_0 + \theta_1 \cdot x$$

Donde:
- $\theta_0$ (intercepto): punto donde la recta corta al eje Y
- $\theta_1$ (pendiente): representa el cambio en Y por cada unidad de cambio en X

## Métodos de Implementación

Existen tres aproximaciones principales para resolver el problema:

1. **Descenso del Gradiente No Matricial**:
   - Implementación iterativa usando bucles
   - Más intuitivo pero menos eficiente computacionalmente

2. **Descenso del Gradiente Matricial**:
   - Utiliza álgebra lineal para optimizar cálculos
   - Más eficiente para grandes conjuntos de datos

3. **Mínimos Cuadrados Analítico**:
   - Solución directa usando ecuaciones normales
   - Óptimo para datasets pequeños/medianos

## Visualización y Evaluación

### Representación Gráfica
Ayuda visualizar:
- La nube de puntos (datos originales)
- La recta de regresión ajustada

### Evaluación del Modelo: Coeficiente de Determinación ($R^2$)

El $R^2$ es una métrica que varía entre 0 y 1, donde:

- $R^2 = 1$: Ajuste perfecto (todos los puntos sobre la recta)
- $R^2 = 0$: No existe relación lineal
- $R^2 \approx 0.8$: Ajuste considerado bueno en muchos contextos
- $R^2 < 0.2$: Ajuste pobre, sugiere relación no lineal o ausencia de relación

## Precauciones y Consideraciones

### Correlación vs Causalidad

Es crucial entender que:

1. La correlación no implica causalidad
2. Pueden existir correlaciones espurias (falsas correlaciones)
3. La interpretación del $R^2$ debe considerar el contexto específico:
   - En ciencias sociales, un $R^2$ de 0.7 puede estar bien
   - En física experimental, se esperan valores mucho más altos