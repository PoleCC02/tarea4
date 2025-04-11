import numpy as np  

# Definir las posiciones de los peces  
loc = np.array([  
    [0, 0, 0],  
    [1, 1, 2],  
    [0, 0, 0],  
    [2, 1, 3],  
    [5, 5, 4],  
    [5, 0, 0],  
    [5, 0, 0],  
    [0, 0, 0],  
    [2, 1, 3],  
    [1, 3, 1]  
])  

# Generar pesos aleatorios para los peces  
generator = np.random.default_rng(1010)  
weights = generator.normal(size=10)  

print("Pesos de los peces:", weights)  

# Sistema para rastrear supervivencia de peces en celdas  
celdas_ocupadas = {}  
for pez in np.range(len(loc)):
    i, j, k = loc[pez]
    posicion = (i, j, k)
    if posicion in celdas_ocupadas
    
