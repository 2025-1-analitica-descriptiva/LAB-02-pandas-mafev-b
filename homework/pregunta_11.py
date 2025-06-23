"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    path_file = "files/input/tbl1.tsv"
    df = pd.read_csv(path_file, sep='\t')
    
    # Agrupa el DataFrame por la columna 'c0'.
    # Para cada grupo, aplica una función a la columna 'c4'.
    # La función lambda ordena los valores de 'c4' y los une en una sola cadena de texto,
    # separada por comas.
    # Finalmente, reset_index() convierte el resultado agrupado de nuevo en un DataFrame.
    resultado = df.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(x))).reset_index()
    
    return resultado

if __name__ == "__main__":
    print(pregunta_11())