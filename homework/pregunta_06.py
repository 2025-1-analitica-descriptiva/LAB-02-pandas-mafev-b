"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    path_file = "files/input/tbl1.tsv"
    df = pd.read_csv(path_file, sep='\t')

    # Get the unique values from column 'c4'.
    unique_values = df['c4'].unique()

    # Convert all values to uppercase.
    uppercase_values = [value.upper() for value in unique_values]

    # Sort the list alphabetically.
    sorted_values = sorted(uppercase_values)

    return sorted_values

if __name__ == "__main__":
    print(pregunta_06())
