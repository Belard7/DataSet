import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
data = pd.read_csv("C:/Users/Jimmy/Documents/DataSet/Lab2/MarvelVsDC.csv")

# Filtrar las columnas necesarias
data_filtered = data[['Movie', 'IMDB_Score']]

# Eliminar entradas con puntajes de IMDB iguales a 0
data_filtered = data_filtered[data_filtered['IMDB_Score'] > 0]

# Seleccionar las primeras 20 películas
data_top10 = data_filtered.head(20)

# Crear el gráfico circular
plt.figure(figsize=(10, 10))
plt.pie(data_top10['IMDB_Score'], labels=data_top10['Movie'], autopct='%1.1f%%', startangle=90)
plt.title('Puntuacion IMDB  por Película (Top 20)')
plt.axis('equal')  # Para asegurar que el gráfico sea circular
plt.show()

#https://www.kaggle.com/datasets/willianoliveiragibin/marvel-vs-dc

#el gráfico proporciona una visión rápida sobre cómo se valoran las películas en función de sus puntajes IMDB, destacando cuáles son las
#más populares y cuáles tienen margen de mejora. Esto puede ayudar a identificar patrones de éxito dentro de la base de datos de películas.