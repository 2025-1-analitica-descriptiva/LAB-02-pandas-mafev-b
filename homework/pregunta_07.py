"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    path_file = "files/input/tbl0.tsv"
    df = pd.read_csv(path_file, sep='\t')
    
    sum_c2_by_c1 = df.groupby('c1')['c2'].sum().sort_index()
    
    return sum_c2_by_c1

if __name__ == "__main__":
    print(pregunta_07())

