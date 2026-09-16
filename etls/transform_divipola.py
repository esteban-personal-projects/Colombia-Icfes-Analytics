import pandas as pd
import unicodedata
import re

df_divipola = pd.read_csv(r"C:\Proyectos Personales\colombia icfes analytics\data\data_raw\codigos_divipola.csv", sep=",",
                          dtype={"Código Departamento": str, "Código Municipio": str})


def limpiar_columna(nombre):
    nombre = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore').decode('utf-8')
    nombre = nombre.strip()
    nombre = re.sub(r'\s+', '_', nombre)
    nombre = nombre.replace('"', '').replace("'", '')
    return nombre.upper()

df_divipola.columns = [limpiar_columna(col) for col in df_divipola.columns]

df_divipola = df_divipola.drop(columns=df_divipola.columns[4]) 

df_divipola['DIVIPOLA_SK'] = range(1, len(df_divipola) + 1)

df_divipola['LATITUD'] = df_divipola['LATITUD'].str.replace(',', '.', regex=False).astype('float64')
df_divipola['LONGITUD'] = df_divipola['LONGITUD'].str.replace(',', '.', regex=False).astype('float64')


cols = ['DIVIPOLA_SK'] + [c for c in df_divipola.columns if c != 'DIVIPOLA_ID']
df_divipola = df_divipola[cols]


df_divipola.to_csv(r"C:\Proyectos Personales\colombia icfes analytics\data\data_cleaned\dim_divipola.csv", index=False)