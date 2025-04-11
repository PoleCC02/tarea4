import numpy as np  

# Crear arreglo 3D de ceros de 10x10x10  usando numpy
arreglo = np.zeros((10, 10, 10), dtype=int)  

# Función para verificar si un número es primo  
def es_primo(n):  
    if n < 2:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

# un loop for para identificar a los pares e impars 
for i in range(10):  
    for j in range(10):  
        for k in range(10):  
            if i % 2 == 1 and j % 2 == 0 and k in [2, 3, 5, 7]:  
                arreglo[i, j, k] = 1   

# imprimier el resultado  
print(arreglo)  