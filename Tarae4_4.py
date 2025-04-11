#Abrir numpy
import numpy as np  

def cambiar_tres(examenes):  
     
    examenes_np = np.array(examenes)  
    
    # Encontrar los valores menores a 60  
    valores_bajos = np.where(examenes_np < 60)[0]   
    
    # Reemplazar los tres primeros valores menores a 60 por ceros  
    for i in range(min(3, len(valores_bajos))):   
        examenes_np[valores_bajos[i]] = 0 
    
    return examenes_np  

# Ejemplo de uso  
resultados_examenes = [80, 40, 55, 71, 25, 95, 54]  
resultados_actualizados = cambiar_tres(resultados_examenes)  

print(resultados_actualizados) 