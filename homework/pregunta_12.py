"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    path_file = "files/input/tbl2.tsv"
    tbl2 = pd.read_csv(path_file, sep='\t')
    
    # Crea una nueva columna 'c5' combinando 'c5a' y 'c5b'.
    # Es necesario convertir la columna 'c5b' a tipo string para poder concatenarla.
    tbl2['c5'] = tbl2['c5a'] + ':' + tbl2['c5b'].astype(str)
    
    # Agrupa por 'c0', luego para cada grupo toma la columna 'c5',
    # ordena sus valores alfabéticamente y únelos en una sola
    # cadena de texto separada por comas.
    resultado = tbl2.groupby('c0')['c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    
    return resultado

if __name__ == "__main__":
    print(pregunta_12())

