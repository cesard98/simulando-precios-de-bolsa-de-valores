# simulando-precios-de-bolsa-de-valores
En este proyecto se usará el movimiento Browniano para simular precios de distintos índices de la Bolsa de Valores, tales como el Índice de precios al consumidor (IPC) y el Standard Poor’s 500 (S&amp;P 500), que son dos de los indicadores más representativos y confiables del estado del mercado accionario mexicano y mundial. A esto se le aplicará el método de Montecarlo para conseguir un resultado más aproximado de la simulación.

<h1>Proceso de Wiener</h1>

El proceso de Wiener es un proceso estocástico de tiempo continuo de valor real, nombrado así por el matemático americano Norbert Wiener por sus investigaciones sobre el movimiento browniano unidimensional y sus propiedades. 

Normalmente al proceso de Wiener se le nombra también movimiento browniano debido a su relación histórica con el proceso físico observado originalmente por Robert Brown. Es uno de los procesos de Lévy mas conocidos y ocurre frecuentemente en matematicas aplicadas, economía, finanzas cuantitativas y física.

El proceso de Wiener normalmente se representa por *W*<sub>*t*</sub> y tiene de características las siguientes propiedades:

1.  *W*<sub>0</sub> = 0

2.  *W* tiene incrementos independientes

3.  *W* tiene incrementos gaussianos:
    *W*<sub>*t* + *u*</sub> − *W*<sub>*t*</sub> se distribuye
    normalmente con media 0 y varianza *u*,
    *W*<sub>*t* + *u*</sub> − *W*<sub>*t*</sub> ∼ 𝒩(0,*u*)

4.  *W*<sub>*t*</sub> es continuo en *t*

El proceso de Wiener se puede construir como el límite de escala de una caminata aleatoria u otros procesos estocásticos de tiempo discreto con incrementos independientes estacionarios. Al igual que la caminata aleatoria, el proceso de Weiner es recurrente en una o dos dimensiones.

<h1>Movimiento browniano geométrico </h1>

El movimiento browniano geométrico (GBM) es un proceso estocástico de tiempo continuo en el que el logaritmo de la cantidad variable aleatoriamente sigue el proceso de Wiener con retornos esperados.

Es un ejemplo importante de procesos estocásticos que satisfacen una ecuación diferencial estocásticas (SDE), se utiliza particularmente en finanzas matemáticas para modelar los precios de las acciones

Para definir un proceso estocástico *S*<sub>*t*</sub> que sigue un GBM
tiene que satisfacer la siguiente ecuación diferencial estocástica:

<strong><blockquote>dS<sub>t</sub> = μS<sub>t</sub>dt + σS<sub>t</sub>dW<sub>t</sub></blockquote></strong>

Donde *W*<sub>*t*</sub> es el proceso de Wiener o movimiento browniano, *μ* es el valor de los retornos esperados del índice y *σ* es la volatilidad en términos anuales.

Al resolver la SDE obtenemos lo siguiente.

<strong><blockquote>*S*<sub>*t*</sub> = *S*<sub>0</sub>*e**x**p*((*μ*−0.5*σ*<sup>2</sup>)*dt*+*σ**d**W*<sub>*t*</sub>)</blockquote></strong>
 
 Esta será la ecuación que se usará para realizar la simulación.


<h1>Simulando precios para el IPC</h1>

Una vez que se resolvió la ecuación diferencial estocástica, se computó un programa en python para realizar la simulación de los precios para el Índice de Precios al Consumidos (IPC) que es uno de los índices más importantes de la bolsa mexicana de valores. La base de datos se obtiene de 'Yahoo Finance' y graficados se ven de esta manera, ver a continuación.

![IPC_data](https://user-images.githubusercontent.com/77253866/153319596-11fb5652-c0e2-4573-ac80-628ac98d4d55.png)

Se simularon 10 posibles caminos de 70 días para el precio del IPC, considerando lo retornos esperados y volatilidad del IPC del último año. Entre más caminos se simulen más exacto será el cálculo de factor de riesgo.

![IPC_mb](https://user-images.githubusercontent.com/77253866/153319689-c4fc1a2f-5570-4275-b51a-129ef7e3151f.png)

Podemos observar que como en el ultimo año los precios del IPC han mantenido una tendencia alcista, esto se ve reflejado en la simulación. Para que esto sea mas visual, se concatenan las dos gráficas.

![IPC_simulacion](https://user-images.githubusercontent.com/77253866/153319727-91ad5790-fe7d-4bd6-a5da-66a3f4dd3c76.png)

<h1> Simulando precios para el S&P 500</h1>

Asimismo, haciendo uso del programa en python antes mencionado, se simularon los índices bursátiles del Índice Standar & Poor’s 500, o bien, el S&P 500, siendo el indicador más representativo de la situación real del mercado estadounidense. También se notó una evidente tendencia alcista en la simulación de 10 posibles caminos en 70 días en el precio de dicho índice.

![SP500_simulacion](https://user-images.githubusercontent.com/77253866/153319834-73efa80b-5fd6-4292-984e-1d48c5b97926.png)

