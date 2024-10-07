import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV

df = pd.read_csv("C:/Users/Jimmy/Documents/DataSet/Lab2/laptops.csv")

# Tipo de cambio de rupias a dólares (aproximado)
exchange_rate = 83  # 1 USD = 83 ₹

# Convertir los precios a dólares
df['Price_USD'] = df['Price'] / exchange_rate

# Agrupar por marca y calcular el precio promedio en dólares
brand_price_avg_usd = df.groupby('Brand')['Price_USD'].mean().sort_values()

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
brand_price_avg_usd.plot(kind='line', marker='o', color='blue')
plt.title('Precio Promedio de Laptops por Marca (en USD)')
plt.xlabel('Marca')
plt.ylabel('Precio Promedio (en $)')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()

# Mostrar gráfico
plt.show()

#https://www.kaggle.com/datasets/pradeepjangirml007/laptop-data-set


#Este análisis nos permite identificar las marcas que ofrecen laptops más accesibles y aquellas que apuntan a un mercado más exclusivo. 
#Es útil para entender el posicionamiento de las marcas en el mercado de laptops