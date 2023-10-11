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

## Análisis de correlación

![]()
