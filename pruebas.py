import numpy as np
import cv2

# Cargar la imagen
imagen = cv2.imread("C:\Users\k_iki\OneDrive\Documentos\Universidad\OctavoSemestre\Dispositivos Médicos\ProyectoGit\Fondos\C_image.jpg")
#Obtener las dimensiones de la imagen
alto, ancho, _ = imagen.shape

# Definir el ancho de la matriz de ceros
ancho_ceros = 200

# Redimensionar la imagen
resized = cv2.resize(imagen, (ancho + ancho_ceros, alto))

# Crear la matriz de ceros
matriz_ceros = np.zeros((alto, ancho_ceros, 3), dtype=np.uint8)

# Concatenar la imagen y la matriz de ceros
imagen_resultante = np.concatenate((resized, matriz_ceros), axis=1)

# Mostrar la imagen resultante
cv2.imshow("Imagen con matriz de ceros", imagen_resultante)
cv2.waitKey(0)
cv2.destroyAllWindows()