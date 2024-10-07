import matplotlib.pyplot as plt
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("C:/Users/Jimmy/Documents/DataSet/Lab2/gymMembers.csv")

# Crear grupos de edades
bins = [0, 18, 25, 30, 35, 40, 45, 50, 100]  # Define los rangos de edad
labels = ['0-18', '19-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Contar la cantidad de personas por género en cada grupo de edad
gender_age_counts = df.groupby(['Age Group', 'Gender']).size().unstack(fill_value=0)

# Graficar la cantidad de personas por género en cada grupo de edad
gender_age_counts.plot(kind='bar', stacked=False)

# Añadir título y etiquetas
plt.title("Cantidad de Personas por Género y Grupo de Edad")
plt.xlabel("Grupo de Edad")
plt.ylabel("Número de Personas")

# Mostrar la gráfica
plt.show()


#https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data

# proporciona una visión general de la composición demográfica de los miembros del gimnasio. La identificación
# de tendencias y patrones en la participación por edad y género puede informar las estrategias de marketing

