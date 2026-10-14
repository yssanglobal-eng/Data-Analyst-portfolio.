import pandas as pd 

#cargar dataset de productos 
df = pd.read_csv("products.csv")

# mostrar las primeras 5 filas 
print(df.head())

# mostrar las últimas 5 filas
print(df.tail()) 