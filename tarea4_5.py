import numpy as np  

# Definir las posiciones de los peces  
locs = np.array([  
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
for index, loc in enumerate(locs):
    pos = tuple (loc)
    if pos not in celdas_ocupadas:
        celdas_ocupadas[pos] = []
    celdas_ocupadas[pos].append(weights[index])

sobreviven  = {}
for posicion, weights_list in celdas_ocupadas.items():
    max_weight = max(weights_list)
    sobreviven [posicion] = max_weight

print ("\n Peces sobrevivientes (posición y peso):")
for posicion, weight in sobreviven.items ():
    print(f"Posición: {posicion}, Peso: {weights}"
          )