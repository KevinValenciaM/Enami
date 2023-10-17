## Creacion de set de datos

Se tienen datos con distinta periodicidad, estos son:

-Variables en línea, muestreo cada 5 min:  
Flujo Aire [N m3/m]  
Enriquecimiento O2 [%]  
Alimentación Concentrado [TPH]  
Alimentacion Si02 [TPH]  
Alimentacion Carga Fria [TPH]  
Coef_o2   
Temperatura M.B. [°C]  
Temperatura Esc. [°C]  

-Variables de laboratorio:  
Muestreo por dia:  
Ley Concentrado S [%]  
Ley Concentrado Cu [%]  
Muestreo cada 3 horas aproximadamente
Ley Cu M.B. [%]  
Ley Fe304 Esc. [%]  
 
Debido a la diferencia de periodicidad de datos se realiza lo siguiente:  
Al tener muestras por día se realiza un relleno de datos con ese valor cada 5 minutos y para muestras con varios valores por día , se realiza un relleno de datos faltantes con el valor siguiente más cercano (backfill).

Ademas se genera un filtro para eliminar outlayers y analisar los momentos en los que se encuentra trabajando el C.T. con concentrado, esto corresponde a un filtro de la tasa de alimentación entre Q1 Y Q3(28,1 TPH a 89,3 TPH).

El codigo de creacion de dataset se encuentra en un notebook con el paso a paso desde los archivos entregados por Enami: [Creacion dataset]((https://github.com/KevinValenciaM/Enami/blob/main/Modelo_de_sugerencia_operacional/Cracion_de_dataset.ipynb))

## Análisis de correlación

![](https://github.com/KevinValenciaM/Enami/blob/main/Modelo_de_sugerencia_operacional/correlacion.png)

Del grafico de correlación se puede ver que existe:  
correlación entre Ley cu y alimentación Sio2(-0.21)  
correlación Ley Fe304 y Concentrado de S(0.2)  
Cruce de temperatura desde cámaras:  
Correlación temperatura promedio mínima con alimentación carga fría(0.25)  
Correlación temperatura promedio y máxima con Alimentación Sio2(0.22 y 0.28)  

## Análisis de temporalidad

El objetivo de este análisis es determinar el tiempo de respuesta de la temperatura en base a los cambios en las variables de entrada del sistema.  
El análisis se realiza para 1021 periodos donde hubo continuidad operacional del C.T.
Se registran los momentos de máximo peak de correlación en cada periodo.
Se genera un gráfico con un histograma de peaks de correlacion de todos los periodos.

![](https://github.com/KevinValenciaM/Enami/blob/main/Modelo_de_sugerencia_operacional/temporalidad.PNG)

No se encuentra un tiempo común de desfase de temperatura
[Codigo analisis temporal](https://github.com/KevinValenciaM/Enami/blob/main/Modelo_de_sugerencia_operacional/temporalidad.PNG)
## Árbol de desición

Búsqueda de parámetros de las variables que repercutan en una mejora del proceso mediante la metodología de un árbol de decisión.
Ingresando las nuevas variables de temperatura al árbol se observa que puede existir una relación influyente para mantener la calidad de las salidas tanto para la ley de cobre en M.B. como la Magnetita en la escoria, sin embargo, hay que considerar que los datos para estas pruebas son pocos.

![](https://github.com/KevinValenciaM/Enami/blob/main/Modelo_de_sugerencia_operacional/arbol.PNG)



