import numpy as np 
#Dar lo valores alaeatorios y presentar una seed 
np.random.seed(0)

puntuaciones = np.random.randint (0, 101, size = 10)
print ("Puntaciones de amor", puntuaciones)

#Matriz de diferencias de puntuaciones
dif = np.abs (puntuaciones[:, np.newaxis]- puntuaciones)
print("Matriz de fierencias", dif)