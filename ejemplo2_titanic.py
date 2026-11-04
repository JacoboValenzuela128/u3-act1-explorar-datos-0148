import pandas as pd
import os

# URL del conjunto de datos
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
# Descargar y cargar
datos = pd.read_csv(url)
# Guardar el archivo "Titanic.csv" en la carpeta datasets
datos.to_csv("datasets/titanic.csv", index=False)
# Explorar información
print("PRIMEROS 5 PASAJEROS")
print(datos.head())
print("\\nDIMENSIONES")
print(datos.shape)
print("\\nCOLUMNAS")
print(datos.columns.tolist())
print("\\nINFORMACION GENERAL")
print(datos.info())
# Identificar características
columnas = ["pclass", "sex", "age", "fare", "sibsp", "parch"]
X = datos[columnas]
# Identificar variable objetivo
y = datos["survived"]
print("\\nCARACTERISTICAS (X)")
print(X.head())
print("\\nVARIABLE OBJETIVO (y)")
print(y.head())
print("\\nCANTIDAD DE SUPERVIVIENTES")
print(y.value_counts())
print("\\nVALORES FALTANTES")
print(datos.isnull().sum())