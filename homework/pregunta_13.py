"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    # Cargar los datos de los archivos en DataFrames
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep='\t')
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep='\t')
    
    # Unir (merge) los dos DataFrames usando la columna 'c0' como clave.
    # Esto crea una tabla combinada donde cada fila tiene la información
    # correspondiente de tbl0 y tbl2.
    merged_df = pd.merge(tbl0, tbl2, on='c0')
    
    # Agrupar el DataFrame combinado por los valores de la columna 'c1' (de tbl0).
    # Luego, para cada grupo, seleccionar la columna 'c5b' (de tbl2) y calcular su suma.
    suma_por_c1 = merged_df.groupby('c1')['c5b'].sum()
    
    return suma_por_c1

if __name__ == "__main__":
    print(pregunta_13())

