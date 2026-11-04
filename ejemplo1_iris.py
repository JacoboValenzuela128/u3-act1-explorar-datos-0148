import pandas as pd
import os
# Arath Valenzuela NC:0148 (4/11/26)
# URL del dataset público para leer datos de iris.csv
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)
print(datos)
# Guardar una copia local
datos.to_csv("datasets/iris.csv", index=False)
# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head())
print()
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)
print("Mostrando nombres de las columnas")
print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())
print("\\nINFORMACION DEL DATASET (Conjunto de datos)")
print(datos.info())
print("\\nCARACTERISTICAS (X) tumba  la columna especies con drop")
X = datos.drop(columns=["species"])
print(X.head())
print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())
print("\\nESPECIES REGISTRADAS")
print(y.unique())